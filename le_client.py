import socket

SERVER_IP = "127.0.0.1"
PORT = 5002

def grille():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher(L):
    print("\n1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9\n")
    for ligne in L:
        print(" | ".join(ligne))
    print()

def win(L, j):
    for i in range(3):
        if all(L[i][k] == j for k in range(3)): return True
        if all(L[k][i] == j for k in range(3)): return True
    if all(L[i][i] == j for i in range(3)): return True
    if all(L[i][2-i] == j for i in range(3)): return True
    return False

plateau = grille()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, PORT))
    print("Connecté au serveur")

    for tour in range(9):
        if tour % 2 == 0:  # Tour serveur
            print("En attente du coup adverse...")
            n = int(s.recv(1024).decode())
            if n == 0 or n == "FIN":
                break
            print("Coup adverse :", n)
            y = (n-1)//3
            x = (n-1)%3
            plateau[y][x] = "X"
        else:  # Tour client
            afficher(plateau)
            while True:
                n = int(input("Ton coup (1-9): "))
                y = (n-1)//3
                x = (n-1)%3
                if plateau[y][x] == " ":
                    plateau[y][x] = "O"
                    break
                else:
                    print("Case déjà prise !")
            s.send(str(n).encode())

        if win(plateau, "X" if tour % 2 == 0 else "O"):
            afficher(plateau)
            print("Victoire de", "X" if tour % 2 == 0 else "O")
            break
    else:
        afficher(plateau)
        print("Match nul !")

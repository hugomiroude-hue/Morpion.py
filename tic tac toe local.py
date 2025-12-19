import socket

HOST = "0.0.0.0"
PORT = 5002

def grille():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher(L):
    print("\n1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9\n")
    for ligne in L-1:
        print(" | ".join(ligne))
        print("---------")
    print()

def win(L, j):
    for i in range(3):
        if all(L[i][k] == j for k in range(3)): return True
        if all(L[k][i] == j for k in range(3)): return True
    if all(L[i][i] == j for i in range(3)): return True
    if all(L[i][2-i] == j for i in range(3)): return True
    return False

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("En attente de connexion...")
conn, addr = server.accept()
print("Connecté à", addr)

plateau = grille()
joueur = "X"

for tour in range(9):
    afficher(plateau)

    if tour % 2 == 0:  # Tour du serveur
        while True:
            n = int(input("Ton coup (1-9): "))
            y = (n-1)//3
            x = (n-1)%3
            if plateau[y][x] == " ":
                plateau[y][x] = joueur
                break
            else:
                print("Case déjà prise !")
        # Envoyer le coup au client
        conn.send(str(n).encode())
    else:  # Tour du client
        print("En attente du coup adverse...")
        n = int(conn.recv(1024).decode())
        print("Coup adverse :", n)
        y = (n-1)//3
        x = (n-1)%3
        plateau[y][x] = "O"

    if win(plateau, joueur if tour % 2 == 0 else "O"):
        afficher(plateau)
        print("Victoire de", joueur if tour % 2 == 0 else "O")
        break
else:
    afficher(plateau)
    print("Match nul !")

conn.send(b"FIN")
conn.close()
server.close()

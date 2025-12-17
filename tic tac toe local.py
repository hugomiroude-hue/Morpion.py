import socket, time

HOST = "0.0.0.0" 
PORT = 5000

def grille():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher(L):
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print()
    for ligne in L:
        print(ligne)

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
for i in range (1000):
    if conn and addr == server.accept():
        break
    else:
        print("En attente de connexion...")
        conn, addr = server.accept()
        print("Connecté à", addr)
        time.sleep(1) 


plateau = grille()

for tour in range(9):
    afficher(plateau)

    if tour % 2 == 0:
        n = int(input("Ton coup (1-9): "))
        conn.send(str(n).encode())
        joueur = "X"
    else:
        n = int(conn.recv(1024).decode())
        print("Coup adverse:", n)
        joueur = "O"

    y = (n-1)//3
    x = (n-1)%3
    plateau[y][x] = joueur

    if win(plateau, joueur):
        afficher(plateau)
        print("Victoire de", joueur)
        break

conn.close()
server.close()

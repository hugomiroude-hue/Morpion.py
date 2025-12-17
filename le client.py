import socket
import time

SERVER_IP = "10.21.0.57"  # ⚠️ Remplace par l'adresse IP du serveur
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, PORT))
    print("Connecté au serveur")

    for i in range(1, 10):
        s.sendall(str(i).encode())
        print("Envoyé :", i)
        time.sleep(1)
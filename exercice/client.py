import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 5001))

c.send("Salut serveur".encode())

reponse = c.recv(1024).decode()
print("Serveur :", reponse)

c.close()
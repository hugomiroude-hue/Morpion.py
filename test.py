import socket
s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen(1)
print("Serveur prêt")
c, a = s.accept()
print("Client connecté :", a)

import socket
c = socket.socket()
c.connect(("10.21.0.56", 5000))
print("Connexion OK")
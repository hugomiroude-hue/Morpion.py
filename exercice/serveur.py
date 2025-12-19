import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 5001))
s.listen(1)

client, addr = s.accept()

msg = client.recv(1024).decode()
print("Client :", msg)

client.send("Message reçu 👍".encode())

client.close()
s.close()
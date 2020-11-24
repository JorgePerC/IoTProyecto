import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("0.0.0.0", 6969))
s.send(b"GET / HTTP/1.1\r\n\r\n")
data = s.recv(1024)
print(data)
s.close()

#---
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 6969))
s.listen(1)
conn, addr = s.accept()
with conn:
    dataFromClient = conn.recv(1024)
    print(dataFromClient)
    conn.send(b"OK")

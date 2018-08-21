from threading import *
import socket

host='127.0.0.1'
port=8000

s=socket(AF_INET, SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print("connected by",addr)
while True:
	data = conn.recv(1024)
	print("received:", repr(data.decode('utf-8')))
	reply= input("Reply:")
	conn.sendall(reply.encode('utf-8'))
conn.close()

T1 = Thread(target = data).start()
T2 = Thread(target = data).start()

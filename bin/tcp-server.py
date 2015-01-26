#! /usr/local/bin/python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)
BUFFSIZE = 1024;
user_name = 'guest'

conn = [];
msg = ['', '']

server_socket = socket(AF_INET , SOCK_STREAM);
print "Server started"
server_socket.bind(ADDR);
print "Listening to port %s" % (PORT)
server_socket.listen(5);

while True:
	connection, addr = server_socket.accept();
	conn.append(connection);
	connection, addr1 = server_socket.accept();
	conn.append(connection);
	while True:
		data = conn[0].recv(BUFFSIZE);
		if not data:
			break;
		msg[0] = "[%s] %s: %s" % (ctime(), user_name, data);
		conn[1].send(msg[0]);

		data = conn[1].recv(BUFFSIZE);
		if not data:
			break;
		msg[1] = "[%s] %s: %s" % (ctime(), user_name, data);
		conn[0].send(msg[1]);


	conn[0].close();
	conn[1].close();

server_socket.close();	

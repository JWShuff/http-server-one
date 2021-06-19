import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # so you don't have to change ports when restarting
server.bind(('localhost', 9292))
print('Waiting For Connection...')
server.listen()

(client_connection, _client_address) = server.accept()
print('New Connection received!')
data = client_connection.recv(1024).decode()
print(data)

client_connection.sendall(b"HTTP/1.1 200 OK\n"
         +b"Content-Type: text/html\n"
         +b"\n" # Important!
         +b"<html><body>Hello World</body></html>\n")

client_connection.close()

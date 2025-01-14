import socket
import datetime
from request import Request

def build_html_response(text_body):
    html_body = f'<html><head><title>JWS HTTP Server</title></head><body>{text_body}</body></html>'
    return f"HTTP/1.1 200 OK \r\nContent-Type:text/html\r\nContent-Length:{len(html_body)}\r\n\r\n{html_body}"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # so you don't have to change ports when restarting
server.bind(('localhost', 9292))

def current_time():
    time = datetime.datetime.now()
    cur_time = time.strftime("%H:%M")
    print(cur_time)
    return cur_time

while True:
    print('Waiting For Connection...')
    server.listen()

    (client_connection, _client_address) = server.accept()
    client_request = Request(client_connection)
    if client_request.parsed_request['uri'] =='/':
        client_connection.send(build_html_response("Hello World!").encode())
    elif client_request.parsed_request['uri'] == '/time':
        cur_time = current_time()
        client_connection.send(build_html_response(f"The current time is {cur_time}").encode())

    client_connection.close()
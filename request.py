class Request:
    def __init__(self, request_text):
        self.parse_request(request_text.recv(4096).decode('utf-8').split('\r\n'))
        print(request_text.recv(4096).decode('utf-8').split('\r\n'))

    #['GET /time HTTP/1.1', 'User-Agent: PostmanRuntime/7.28.0', 'Accept: */*', 'Postman-Token: e928f7d6-ed77-4eb9-858c-ebdd3448709c', 'Host: localhost:9292', 'Accept-Encoding: gzip, deflate, br', 'Connection: keep-alive', '', '']
    def parse_request(self, decoded_request_text):
        print(decoded_request_text[1]) #Gotta figure out how to grab these key/value pairs to run into the object
        self.parsed_request = {}
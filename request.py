class Request:
    def __init__(self, request_text):
        self.parse_request(request_text.recv(4096).decode('utf-8').split('\r\n'))

    #['GET /time HTTP/1.1', 'User-Agent: PostmanRuntime/7.28.0', 'Accept: */*', 'Postman-Token: e928f7d6-ed77-4eb9-858c-ebdd3448709c', 'Host: localhost:9292', 'Accept-Encoding: gzip, deflate, br', 'Connection: keep-alive', '', '']
    def parse_request(self, decoded_request_text):
        self.parsed_request = {}
        self.parsed_request['uri'] = decoded_request_text.pop(0).replace("GET ", "").replace(" HTTP/1.1", "")
        for item in decoded_request_text:
            if item == "":
                continue
            split_item = item.split(': ')
            print(split_item)
            self.parsed_request[split_item[0]] = split_item[1]
        
        print(self.parsed_request)
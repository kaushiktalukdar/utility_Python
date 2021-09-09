import socket

"""
SERVER V2 : consider scalability

1) Ref

Sockets are byte streams, not message streams
http://stupidpythonideas.blogspot.com/2013/05/sockets-are-byte-streams-not-message.html

2) Commands
python server.py

3) client.py
https://github.com/yennanliu/utility_Python/blob/master/stream/client.py

4) QA 
plz use below curl commands send data via CLI
curl -d "param1=value1&param2=value2" -X POST http://localhost:9999
curl -d "123123" -X POST http://localhost:9999
curl -d "HELLO WORLD" -X POST http://localhost:9999
"""
class Server:

    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 9999

        # define recv_bufsize, so we can really receive and cut off on each incoming event
        self.recv_bufsize = 22

    def read_endpoint(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(1)

        while True:
            conn, addr = server.accept()
            """
            https://docs.python.org/3/library/socket.html

            socket.recv(bufsize[, flags])
            Receive data from the socket. 
            The return value is a bytes object representing the data received. 
            The maximum amount of data to be received at once is specified by bufsize. 
            """
            clientMessage = str(conn.recv(self.recv_bufsize), encoding='utf-8')
            print('Client message is:', clientMessage)

            # save to file
            with open('output.txt', 'a') as f:
                f.write(clientMessage)
        f.close()

if __name__ == '__main__':
    s = Server()
    s.read_endpoint()
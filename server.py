import SocketServer
class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        conn = self.request
        print 'connection'
        conn.sendall('Server:hello,gateway!!!')
        Flag = True
        while Flag:
            data = conn.recv(1024)
            print data
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall('hello')
            else:
                conn.sendall('Server:'+data)
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('10.0.1.4',9999),MyServer)
    server.serve_forever()
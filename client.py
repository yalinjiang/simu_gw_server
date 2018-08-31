'''


@author: Administrator
'''
import socket
import sys
 
HOST, PORT = "139.219.132.106", 9999
data = "hello"#.join(sys.argv[1:])
 
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    print data,bytes(data + "\n")
    sock.sendall(bytes(data + "\n"))
 
    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()
 
print("Sent:     {}".format(data))
print("Received: {}".format(received))
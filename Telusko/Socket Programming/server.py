import socket
# Create Socket
s = socket.socket()
print("Socket is created")
# Set IP and Type
s.bind(('localhost',9999))
print("Waiting for Connections....")
#Listen to the clients
s.listen(3)

while True:
    # Accept the connection
    c,add = s.accept()
    
    name = c.recv(1024).decode()
    print("Connected with",add)
    print("Client name is",name)
    c.send(bytes('Welcome to Ratnagiri','utf-8'))
    

    c.close()

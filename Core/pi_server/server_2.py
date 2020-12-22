import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_ADDR_ALL = '' 
IP_PORT = 9800 

BUFFER_SIZE = 16 * 1024 #16 KB blocks

# Bind the socket to the port
serverAddress = (IP_ADDR_ALL, IP_PORT) 
print('Initialazing server in {}, port {}'.format(*serverAddress))
sock.bind(serverAddress) 

sock.listen(10) #Connections in queue

while True:
    # Waiting for connection
    print('Waiting for remote connection')
    connection, clientAddress = sock.accept()
    try:
        print('Connection from', clientAddress)

        while True:
            data = connection.recv(BUFFER_SIZE)
            print('Received: {!r}'.format(data))
            if data: #while receiving it won't close
                print('Waiting for new message')
            else:
                print('Ending connection from', clientAddress)
                break
    
    except KeyboardInterrupt:
        sock.close()

    finally:
        # closing connection
        connection.close()
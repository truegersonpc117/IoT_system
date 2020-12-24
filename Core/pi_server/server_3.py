import socket
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
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
            data=data.decode()#Here we transform the data to a string
            data=data.replace('\r', '')#Here we remove the \r part of the string
            data=data.replace('\n', '')#Here we remove the \n part of the string
            print('Received: {!r}' .format(data))
            if data: #while receiving it won't close
                if data=='on': #condition to activate the relay
                    status=1
                    GPIO.output(2, status)
                else:
                    if data=='off': #condition to deactivate the relay
                        status=0
                        GPIO.output(2, status)
                    else:
                        status=status
                    
            else:
                print('Ending connection from', clientAddress)
                break
    
    except KeyboardInterrupt:
        sock.close()

    finally:
        # closing connection
        connection.close()


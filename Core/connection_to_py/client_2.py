import socket
ms=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ms.connect(('192.168.0.19', 9800))
while True:
    try:
        msg=input("Type your message: ")
        ms.sendall(msg.encode())

    except KeyboardInterrupt:
        ms.close()
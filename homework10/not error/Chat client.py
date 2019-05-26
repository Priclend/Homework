import socket

while True:
    try:
        server_address = ('192.168.100.4',9090)
        simpleSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        simpleSock.connect(server_address)
        print ("Соединение установлено:", server_address)
        

        while True:
            message = input()
            simpleSock.send(message.encode())
            print(simpleSock.recv(1024))

        
    except OSError:
        print ("Пытаемся установить соединение")
      

    


import socket, time

t = time.time()


while True:

    if (time.time() - t) < 10:
        
        try:
            server_address = ('192.168.100.4',9090)
            simpleSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            simpleSock.connect(server_address)
            print ("Соединение установлено:", server_address)
        

            while True:
                print(simpleSock.recv(128).decode('utf-8'))
                message = input()
                simpleSock.send(message.encode('utf-8'))
                    
        except OSError:
            print ("Пытаемся установить соединение")
    else:
        print("Превышено время жидания, попробуйте позже")
        exit ()

    




        
      

    


import socket, time

t = time.time()

def file_get (file):
    data = open ('NewFile.txt', 'w')
    data.write (file)
    data.close ()
    print ('end')   

while True:

    if (time.time() - t) < 10:
        
        try:
            server_address = ('192.168.100.4',9090)
            simpleSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            simpleSock.connect(server_address)
            print ("Соединение установлено:", server_address)
        

            while True:
                print(simpleSock.recv(1024).decode('utf-8'))
                message = input()
                simpleSock.send(message.encode('utf-8'))
                file_get(simpleSock.recv(1024).decode('utf-8'))
                    
        except OSError:
            print ("Пытаемся установить соединение")
    else:
        print("Превышено время жидания, попробуйте позже")
        exit ()

    


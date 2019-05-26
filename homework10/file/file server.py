import os, socket

def createFile (nameFile):
    file = open(nameFile,'w')
    for i in range(100):
        file.write('Hello\n')
    file.close ()
    print ('конец записи')
    
def dataForSending (message):
    return (message.decode('utf-8'))



server_address = ('192.168.100.4',9090)
simpleSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
simpleSock.bind(server_address)
simpleSock.listen(5)
socket_connection, client_address = simpleSock.accept()
print ("Соединение установлено:", client_address)

while True:
    socket_connection.send(b'Name of File')
    message = dataForSending (socket_connection.recv(1024))
    print("получено сообщение:",message)
    createFile (message)
    file_name = message
    file_address = os.path.abspath(file_name)
    file_size = os.path.getsize(file_address)
    size = 1024
    for i in range(round(file_size/size + 0.499)):
        data = f.read(size)
        print(data)
    

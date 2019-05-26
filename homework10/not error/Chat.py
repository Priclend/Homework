import socket

server_address = ('192.168.100.4',9090)
simpleSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
simpleSock.bind(server_address)
simpleSock.listen(1)
socket_connection, client_address = simpleSock.accept()
print ("Соединение установлено:", client_address)


while True:
        message = socket_connection.recv(1024)
        print('Получено сообщение:', message.decode('utf-8'))
        socket_connection.send(b'OK')



    
    

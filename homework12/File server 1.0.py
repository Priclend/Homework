import os, socket

def create_file (nameFile):
    file = open(nameFile,'w')
    for i in range(100):
        file.write('Hello\n')
    file.close ()
    print ('конец записи') #пусть останется здесь, хотя оно нужно только для меня)
    
def dataForSending (message):
    return (message.decode('utf-8'))

def sent_file (nameFile):
    file = open(nameFile,'rb')
    data = file.read()
    socket_connection.send (data)
    message = dataForSending (socket_connection.recv(1024))
    print("получено сообщение:" , message)
    file.close ()

server_address = ('192.168.100.4' , 9090)
simpleSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
simpleSock.bind(server_address)
simpleSock.listen(5)
socket_connection, client_address = simpleSock.accept()
print ("Соединение установлено:" , client_address)

while True:
    socket_connection.send(b'Good day! Wat file yo would like to get? I have: Hello, Dear, New, Vin',)
    message = dataForSending (socket_connection.recv(1024))
    print("получено сообщение:" , message)
    sent_file (message)

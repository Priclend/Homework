def addition (a,b):
    return a + b

def subtraction (a,b):
    return a - b

def multiplication (a,b):
    return a * b

def division (a,b):
    return a / b

def dataForSending (message):
    message = (message.decode('utf-8'))
    return (int(message))


import socket 

server_address = ('192.168.100.4',9090)
simpleSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
simpleSock.bind(server_address)
simpleSock.listen(5)
socket_connection, client_address = simpleSock.accept()
print ("Соединение установлено:", client_address)

while True:
    
    socket_connection.send(b'+ = 1, - = 2, * = 3, / = 4')
    message = dataForSending (socket_connection.recv(128))
    print("получено сообщение:",message)
    
    if  message == 1 :
        socket_connection.send(b'+')
        m1 = dataForSending (socket_connection.recv(128))
        print("Первое число:",m1)
        socket_connection.send(b'ok')
        m2 = dataForSending (socket_connection.recv(128))
        print("Второе число:",m2)
        print ('Ответ:',addition (m1, m2))
        socket_connection.send(str(addition(m1, m2)).encode("utf-8"))
        s = (socket_connection.recv(128))
        
    elif message == 2 :
        socket_connection.send(b'-')
        m1 = dataForSending (socket_connection.recv(128))
        print("Первое число:",m1)
        socket_connection.send(b'ok')
        m2 = dataForSending (socket_connection.recv(128))
        print("Второе число:",m2)
        print ('Ответ:',subtraction (m1, m2))
        socket_connection.send((str(subtraction(m1, m2)).encode("utf-8")))
        s = (socket_connection.recv(128))
        
    elif message == 3 :
        socket_connection.send(b'*')
        m1 = dataForSending (socket_connection.recv(128))
        print("Первое число:",m1)
        socket_connection.send(b'ok')
        m2 = dataForSending (socket_connection.recv(128))
        print("Второе число:",m2)
        print ('Ответ:',multiplication (m1, m2))
        socket_connection.send(str(multiplication(m1, m2)).encode("utf-8"))
        s = (socket_connection.recv(128))
        
    elif message == 4 :
        socket_connection.send(b'/')
        m1 = dataForSending (socket_connection.recv(128))
        print("Первое число:" , m1)
        socket_connection.send(b'ok')
        m2 = dataForSending (socket_connection.recv(128))
        print("Второе число:" , m2)
        print ('Ответ:' , division (m2, m1))
        socket_connection.send(str(division(m1, m2)).encode("utf-8"))
        s = (socket_connection.recv(128))
        
    else:
        socket_connection.send(b'sorry, try again')
        
    
    

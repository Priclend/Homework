def coordinats (a,b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    print ("Расстояние по x", x, "Расстояние по y", y)
n = 2
a = []
b = []

for i in range (n):
    print ('Введите с начала все x, а затем все y')
    a.append ( int(input ()))
    b.append ( int(input ()))

coordinats (a,b)


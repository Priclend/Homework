print ("Введите, пожалуйста, длинну массива.")
n = int (input ())
print ("Введите пожалуйста все числа первого массива.")
a = []
for i in range(n) :
    a.append(int(input ()))

print (a)
print ("А теперь все числа второго массива")
b = []
for i in range(n) :
    b.append(int(input ()))

print (b)

for g in range (len (a)) :
    for h in range (len (b)) :
        print ( a[g] * b[h] )



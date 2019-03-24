d = {}

print ("Введите количество элементов словаря")
n = int(input ())

for i in range (0,n):
    a = input ()
    b = input ()
    d[a] = b
for j in d:
    print (j, ":", d[j])



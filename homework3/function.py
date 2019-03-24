def function_1 (a, b, c):
    global d
    d = int (b**2 - (4*a*c))
    print (d)
    import modul
    modul.function_2 (a, b, d)
    


print ("Введите a")
a = int(input ())
print ("Введите b")
b = int (input ())
print ("Введите c")
c = int (input ())

function_1 (a,b,c)


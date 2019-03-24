def line1 (x) :
    return 5*x+16
'''функции'''


def line2 (x) :
    return 17*x+123


def line3 (x) :
    return 9*x+1


def line4 (x) :
    return 0.2*x-7


def line5 (x) :
    return (1/7)*x+6


def line6 (x) :
    return 5*x-50


def line7 (x) :
    return 13*x-6


def line8 (x) :
    return 57*x+908


def line9 (x) :
    return 12*x+144


def line10(x) :
    return x-8


def increment (funct, x1, x2):
    return funct(x2) - funct(x1)    #приращение



arrayOfFunctions = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
#Массив функций

maxFunct = arrayOfFunctions[0] #задаём максимум первым числом из массива

for i in arrayOfFunctions :
    if increment(i,0,1) > increment(maxFunct, 0, 1): #сравниваем поочерёдно все приращения функций из массива с максимумом
        maxFunct = i # приравниваем i к максимальному значению

print (maxFunct.__name__ ,":", increment(maxFunct, 0, 1)) # выводим имя функции с макс. приращением

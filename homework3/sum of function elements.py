def summ (a):
    b = sum(a)
    print (b)
    
print ("сколько чисел вы хотите сложить?")
n = int (input())
a = []
for i in range(n):
    a.append(int(input()))
print (a)

summ(a)

#sum = сумма всех элементов

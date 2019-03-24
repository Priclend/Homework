def function(x0):
    y1 = x0
    y2 = x0**2
    y3 = x0**3
    def function1 (y1, y2, y3, x0):
        print("Введите x1")
        x1 = int(input())
        Y1 = x1
        Y2 = x1**2
        Y3 = x1**3
        deltaY1 = Y1 - y1
        deltaY2 = Y2 - y2
        deltaY3 = Y3 - y3
        print ("Приращение 1-ой ф-ции =", deltaY1, "Приращение 2-ой ф-ции =", deltaY2, "Приращение 3-ий ф-ции =", deltaY3)
    function1(y1, y2, y3, x0)
print ("Введите, пожалуйста, x")

x0 = int(input())

function(x0)        

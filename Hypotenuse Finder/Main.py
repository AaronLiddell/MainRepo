import math as m

def getData():
    x = int(input("Input side one of triangle: "))
    y = int(input("Input side two of triangle: "))
    hypo(x,y)

def hypo(x,y):
    hypo = m.sqrt(x**2 + y**2)
    print(hypo)

getData()

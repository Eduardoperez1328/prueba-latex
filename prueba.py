# y=[4,15,24,56]
# print "El primero es", y[0], "y el ultimo es", y[3]

# print range(7)

# for i in range(3):
#     print "hola"
#     print "Eduardo"
# print "Hasta Luego"

# y.append("Bye")
# print y

# x=[100]
# for i in range(10):
#     x.append(1.01*x[i])
# print x

# f=[1,1]
# for i in range(15):
#     f.append(f[i]+f[i+1])
#print f

#import matplotlip.pyplot

# def suma(x,y):
#     return x+y

# suma(2,3)

# def producto(x,y):
#     return x*y

# producto(5,5)

# def operacion(x,y,f):
#     return f(x,y)

# operacion(2,3,suma)

# def funcion(x):
#     return 2*x

# def iteracion(inicial,iteraciones,fun):
#     x=[inicial]
#     for i in range(iteraciones):
#         x.append(fun(x[i]))
#     return x

# iteracion(1,50,funcion)

# import math

# iteracion(1,1000,math.sin)

import numpy as np

def diagrama(f, x0, it):
    x = [x0]
    y = [x0]
    s = np.arange(0, 1, 0.01)
    for i in range(it):
        x.append(x[2*i])
        x.append(f(x[2*i]))
        y.append(f(y[2*i]))
        y.append(f(y[2*i]))
    plt.plot(x, y, color = 'red')
    plt.plot(s, f(s))
    plt.plot(s, s, color = 'black')
    plt.show()

def logistica(x):
    return 2*x*(1-x)

diagrama(logistica, 0.1, 100)

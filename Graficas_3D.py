import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


f= lambda x,y:x**2 - y**2  #funcion lambda
x=np.linspace(-5,5,50)
y=np.linspace(-5,5,50)
#---------Declaramos un meshgrid-----: se le pasan los valores de (x,y) y devuelve matrices de coordenadas
X,Y=np.meshgrid(x,y)

#---------------------------------Se grafica una función-----------------------
fig=plt.figure()
ax = plt.axes(projection='3d') 
ax.plot_surface(X,Y,f(X,Y),cmap=cm.copper) #f(X,Y) evaluada en la funcion lambda , cmap=cm.copper solo son los colores de la grafica
ax.view_init(45,45)#vista con la que se va a ver la grafica
plt.title("Silla de montar",  fontdict={'family': 'serif', 'color' : 'green','weight': 'bold','size': 18})
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()

#--------------------------Se grafican dos funciones con subplot-----------------------
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface(X,Y,f(X,Y),cmap=cm.copper)
ax.view_init(45,45)
plt.title("Superficie",  fontdict={'family': 'serif', 'color' : 'blue','weight': 'bold','size': 18})

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.contour(X,Y,f(X,Y),cmap=cm.coolwarm)
ax.view_init(45,45)
plt.title("Curvas de nivel",  fontdict={'family': 'serif', 'color' : 'red','weight': 'bold','size': 18})
plt.show()




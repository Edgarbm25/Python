import matplotlib.pyplot as plt
import numpy as np


#--------------------------------------Caida libre----------------------------------------------

xo=0
vo=0
g=9.81

plt.figure()
t=np.linspace(1,100,100)
y=xo + vo*t -(g*t**2)/2 
v=vo - g*t
a=-g

plt.subplot(1,3,1)
plt.plot(t,y,color='r')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Posición")
plt.grid()

plt.subplot(1,3,2)
plt.plot(t,v,color='g')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Velocidad")
plt.grid()


a=np.ones(np.size(y))*9.81
plt.subplot(1,3,3)
plt.plot(t,-a,color='orange')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Aceleración")
plt.grid()

plt.suptitle("Caida libre")
plt.tight_layout()


#------------------------------Movimiento oscilatorio------------

plt.figure()
w=0.5

grid = plt.GridSpec(2, 3, wspace=0.8, hspace=0.5)

plt.subplot(grid[0, 0])
y_os=np.sin(w*t)
plt.plot(t,y_os)
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Posición")
plt.grid()

plt.subplot(grid[0, 1])
v_os=w*np.cos(w*t)
plt.plot(t,v_os,color='r')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Velocidad")
plt.grid()

plt.subplot(grid[0, 2])
a_os=-w**2*np.sin(w*t)
plt.plot(t,a_os,color='g')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Aceleracion")
plt.grid()


plt.subplot(grid[1, 0:]);
plt.plot(t,y_os,t,v_os,t,a_os)
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.grid()

plt.suptitle("Movimiento armónico simple")



#----------------Movimiento circular uniforme-----------

plt.figure()
R=1
plt.subplot(2,3,1)
x_pol=R*np.cos(w*t)
y_pol=R*np.sin(w*t)
plt.plot(t,x_pol,t,y_pol)
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Posición")
plt.grid()

plt.subplot(2,3,2)
v_polx=R*w*np.cos(w*t)
v_poly=R*w*np.sin(w*t)
plt.plot(t,v_polx,t,v_poly)
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Velocidad")
plt.grid()

plt.subplot(2,3,3)
a_polx=-R*w**2*np.cos(w*t)
a_poly=-R*w**2*np.sin(w*t)
plt.plot(t,a_polx,t,a_poly)
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Aceleracion")
plt.grid()


plt.subplot(2,3,4)
plt.plot(x_pol,y_pol , color='red')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Posición(Fase)")
plt.grid()

plt.subplot(2,3,5)
plt.plot(v_polx,v_poly, color='orange')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Velocidad(Fase)")
plt.grid()

plt.subplot(2,3,6)
plt.plot(a_polx,a_poly, color='green')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Aceleracion(Fase)")
plt.grid()


plt.suptitle("Movimiento circular uniforma")
plt.tight_layout()




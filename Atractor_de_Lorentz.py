
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d

def model(z,t):
    dxdt = 10 *(z[1]-z[0]) 
    dydt = z[0]*(28-z[2])-z[1]
    dzdt = z[0]*z[1] - (8/3)*z[2]
    xp = [dxdt,dydt,dzdt]
    return xp

# Condiciones iniciales
z0 = [0.5,0.9,3] 
n = 22001 #El vector tiene estas dimensiones pata que pueda se ocupado en linspac
# vector de tiempo
t = np.linspace(0,100,n)

# solucionador de  ODE
z = odeint(model,z0,t)

#Grafica en 3D  
fig = plt.figure()

ax = plt.axes(projection='3d') 

x_sol = z[:,0]
y_sol = z[:,1]
z_sol = z[:,2]
ax.plot3D(x_sol, y_sol, z_sol, 'orange')

plt.title("Atractor de Lorentz",  fontdict={'family': 'serif', 'color' : 'darkblue','weight': 'bold','size': 18})

plt.show()


#Comentario d eprueba
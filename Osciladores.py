import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model_Lorenz(z,t):
    dxdt = 10 *(z[1]-z[0]) 
    dydt = z[0]*(28-z[2])-z[1]
    dzdt = z[0]*z[1] - (8/3)*z[2]
    xp = [dxdt,dydt,dzdt]
    return xp

m1=-5/7
m2=-3/7
lamda=30
alpha=15.6

def model_Chua(x,t):
    phix=m1*x[0] + m2*(abs(x[0]+1)-abs(x[0]-1))
    dx1 = alpha*(-x[0] + x[1]- phix) 
    dx2 = x[0]-x[1]+x[2]
    dx3 = -lamda*x[1]
    xp = [dx1,dx2,dx3]
    return xp

a=0.2
b=5
c=0.2

def model_Rossler(x,t):
    dx1 = -x[1]- np.exp(x[2]) 
    dx2 = x[0] + a*x[1]
    dx3 = x[0] + (-b+c*np.exp(-x[2]))
    xp = [dx1,dx2,dx3]
    return xp


# Condiciones iniciales
z0 = [0.5,0.9,3] 
n = 5001 #El vector tiene estas dimensiones pata que pueda se ocupado en linspace
# vector de tiempo
t = np.linspace(0,100,n)

# solucionador de  ODE (Lorenz)
X = odeint(model_Lorenz,z0,t)
x1_sol_Lorenz = X[:,0]
x2_sol_Lorenz = X[:,1]
x3_sol_Lorenz = X[:,2]

# solucionador de  ODE (Chua)
X = odeint(model_Chua,z0,t)
x1_sol_Chua = X[:,0]
x2_sol_Chua = X[:,1]
x3_sol_Chua = X[:,2]

# solucionador de  ODE (Rossler)
X = odeint(model_Rossler,z0,t)
x1_sol_Rossler = X[:,0]
x2_sol_Rossler = X[:,1]
x3_sol_Rossler= X[:,2]

#Grafica en 3D  

fig = plt.figure(figsize=plt.figaspect(0.5))

ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.plot3D(x1_sol_Lorenz, x2_sol_Lorenz, x3_sol_Lorenz, color='orange')
plt.title("Oscilador de Lorenz",color='orange',fontsize=15,fontweight='bold')

ax = fig.add_subplot(1, 3, 2, projection='3d')
ax.plot3D(x1_sol_Chua, x2_sol_Chua, x3_sol_Chua, color='red')
plt.title("Oscilador de Chua",color='red',fontsize=15,fontweight='bold')

ax = fig.add_subplot(1, 3, 3, projection='3d')
ax.plot3D(x1_sol_Rossler, x2_sol_Rossler, np.exp(x3_sol_Rossler), color='green')

plt.title("Oscilador de Rossler",color='green',fontsize=15,fontweight='bold')

plt.show()


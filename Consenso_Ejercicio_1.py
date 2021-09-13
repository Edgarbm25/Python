import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


L=np.array([[2,0,-1,0,-1],
[-1,2,-1,0,0],
[0,-1,1,0,0],
[-1,0,0,1,0],
[0,0,0,0,0],])



# function that returns dy/dt
def model(x,t):
    #dydt = -(np.kron(L,np.identity(1)))*x
    dx1=-(x[0]-x[2]) - (x[0]-x[4])
    dx2=-(x[1]-x[0]) - (x[1]-x[2])
    dx3=-(x[2]-x[1]) 
    dx4=-(x[3]-x[0]) 
    dx5=0
    xp = [dx1,dx2,dx3,dx4,dx5]
         
    return xp

# initial condition
x0 = [0.7,0.2,-0.6,0.1,1]

# time points
t = np.linspace(0,30)

# solve ODE
y = odeint(model,x0,t)


# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel(r'$\sin (x)$')
plt.legend([r'$\xi_1$',r'$\xi_2$',r'$\xi_3$',r'$\xi_4$',r'$\xi_5$'],loc="best")
plt.title('Consenso Ejercicio 1')
plt.grid()
plt.show()
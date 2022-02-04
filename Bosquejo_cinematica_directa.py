import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# function that returns dy/dt
def model(cond_ini,t):
    K=5
    
    xd=0.5
    yd=0.2   
    
    x0=cond_ini[0]
    y0=cond_ini[1]
    theta0=cond_ini[2]
    
    v=K*math.sqrt((x0-xd)**2 + (y0-yd)**2 )
    Theta=math.atan((yd-y0)/(xd-x0))
    
    
    dxdt = v*math.cos(Theta)
    dydt = v*math.sin(Theta)
    d_Theta =Theta 
    
    return dxdt,dydt,d_Theta

# initial condition
cond_ini = [-0.1,0.1,0.5]

# time points
t = np.linspace(0,5)

# solve ODE
y = odeint(model,cond_ini,t)

# plot results
plt.plot(y[:,0],y[:,1])
plt.xlabel('x')
plt.ylabel('y(t)')
plt.show()

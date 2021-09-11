import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


M=1
b=0.1
Kv=1
Kp=5
ref=5
g=9.81

# functions that returns dy/dt

def model_regulacion(y,t):
    dydt1 = y[1]
    dydt2 = -y[1]*(b+Kv)/M - Kp*(y[0]-ref)/M
    dydt=[dydt1,dydt2]
    return dydt


def model_seguimiento(y,t):
    
    ref_seguimiento=np.sin((np.pi/4)*t)
    ref_seguimiento_d=(np.pi/4)*np.cos((np.pi/4)*t)
    
    dydt1 = y[1]
    dydt2 = -(y[1]-ref_seguimiento_d)*(b+Kv)/M - Kp*(y[0]-ref_seguimiento)/M
    dydt=[dydt1,dydt2]
    return dydt



# initial condition
y0 = [0.1,0.1]

# time points
t = np.linspace(0,25)

trayectoria=np.sin((np.pi/4)*t)

# solve ODE
y_regulacion = odeint(model_regulacion,y0,t)
y_seguimiento = odeint(model_seguimiento,y0,t)

# plot results
plt.subplot(1,2,1)
plt.plot(t,y_regulacion)
plt.xlabel('Tiempo')
plt.ylabel('Magnitud')
plt.title('Control de regulación de sistema MRA')
plt.grid()
plt.legend(['Posición','Velocidad'],loc="upper right")
plt.subplot(1,2,2)
plt.plot(t,y_seguimiento,t,trayectoria)
plt.xlabel('Tiempo')
plt.ylabel('Magnitud')
plt.title('Control de seguimiento de sistema MRA')
plt.grid()
plt.legend(['Posición','Velocidad','Trayectoria'],loc="upper right")
plt.show()






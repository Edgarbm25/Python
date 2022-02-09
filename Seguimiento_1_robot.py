import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# function that returns dy/dt
def model(cond_ini,t):
    
    #Parametros
    a=6/5
    zeta=0.5
        
    #Valores de la pose en un instante ti    
    x=cond_ini[0]
    y=cond_ini[1]
    theta=cond_ini[2]
        
    #Referencias de trayectoria deseada 
    xd=np.cos(t/10)
    dxd=-(1/10)*np.sin(t/10)
    ddxd=-(1/100)*np.cos(t/10)
    
    yd=np.sin(t/10)
    dyd=(1/10)*np.cos(t/10)
    ddyd=-(1/100)*np.sin(t/10)
      
    v_d=math.sqrt(dxd**2 + dyd**2)
    theta_d=math.atan2(dyd,dxd)
    omega_d=(ddyd*dxd -ddxd*dyd)/(dxd**2 + dyd**2)
    
    #Ganancias
    k1=2*zeta*a
    k2=(a**2-omega_d**2)/v_d
    k3=k1
    
    #Errores 
    e_x=(xd-x)*np.cos(theta) + (yd-y)*np.sin(theta)
    e_y=-(xd-x)*np.sin(theta) + (yd-y)*np.cos(theta)
    e_theta=theta_d-theta
    
    #Señales de retroalimentacion
    u1=-k1*e_x
    u2=-k2*e_y-k3*e_theta
    
    #Señales de control    
    v=v_d*np.cos(e_theta)-u1
    omega=omega_d-u2
    
    #Modelo cinemático
    
    dxdt=v*np.cos(theta)
    dydt=v*np.sin(theta)
    dtheta=omega
    
    
    return dxdt,dydt,dtheta


t = np.linspace(0,50*np.pi, 100)

#Trayectoria deseada (x,y)
xd=np.cos(t/10)
dxd=-(1/10)*np.sin(t/10)
yd=np.sin(t/10)
dyd=(1/10)*np.cos(t/10)

#Definir la orientacion deseada
theta_d=[]
for i in range(len(t)):
    theta_d.append(math.atan2(dyd[i],dxd[i]))
        
# Condiciones iniciales
cond_ini = [0,0,0]

# Solver
Cinematica = odeint(model,cond_ini,t)

plt.figure()
grid = plt.GridSpec(2, 2, wspace=0.3, hspace=0.5)

plt.subplot(grid[0, 0])
plt.plot(t,xd,t,Cinematica[:,0],label='hola')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Seguimiento en x')
plt.legend(["Trayectoria deseada", "Robot"], loc ="upper right")
plt.grid()

plt.subplot(grid[1, 0])
plt.plot(t,yd,t,Cinematica[:,1])
plt.xlabel('t')
plt.ylabel('y')
plt.title('Seguimiento en y')
plt.legend(["Trayectoria deseada", "Robot"], loc ="upper right")
plt.grid()

plt.subplot(grid[0, 1])
plt.plot(t,theta_d,t,Cinematica[:,2])
plt.xlabel('t')
plt.ylabel('theta')
plt.title('Seguimiento en theta')
plt.legend(["Trayectoria deseada", "Robot"], loc ="upper right")
plt.grid()

plt.subplot(grid[1, 1])
plt.plot(xd,yd,Cinematica[:,0],Cinematica[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Retrato fase')
plt.legend(["Trayectoria deseada", "Robot"], loc ="upper right")
plt.grid()

plt.suptitle("Seguimiento de trayectoria")


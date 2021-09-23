
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


m=2
n=10
gama=5


L = np.array([[2,-1,0,0,0,0,0,0,0,0,-1],
     [-1,2,0,0,0,0,0,0,0,0,-1],
     [0,-1,2,0,0,0,0,0,0,0,-1],
     [0,-1,-1,4,0,-1,0,0,0,0,-1],
     [0,0,0,-1,2,0,0,0,0,0,-1],
     [0,0,0,-1,-1,4,-1,0,0,0,-1],
     [-1,0,0,0,0,0,3,-1,0,0,-1],
     [-1,0,0,0,0,0,0,2,0,0,-1],
     [0,0,0,0,0,0,0,-1,3,-1,-1],
     [-1,0,0,0,0,0,0,0,0,2,-1],
     [0,0,0,0,0,0,0,0,0,0,0]]);


# function that returns dy/dt
def model(x,t):
    delta=[ 0.7071,0,0.5721,0.4156,0.2185,0.6725,-0.2185,0.6725,-0.5721,0.4156,-0.7071,0,-0.5721,-0.4156,-0.2185,-0.6725,0.2185,-0.6725,0.5721,-0.4156,0,0]
    desfase = np.kron(L,np.identity(m))@delta
    dydt = -(gama*np.kron(L,np.identity(m)))@x + desfase
  
    return dydt



t = np.linspace(0,3)
#conidciones iniciales
x0=[0.0097,	0.5322,	0.2793,	0.9462,	0.9064,	0.3926,	0.0248,	0.6714,	0.8371,	0.9714,	0.0569,	0.450,	0.5824,	0.6866,	0.7194,	0.6500,	0.7269,	0.3738, 0.5815,	0.116,0.6,0.8];

# Se resuelve el ODE para que se converja al circulo
y = odeint(model,x0,t)

#se guarda la trayectoria hacia la convergencia en la variable convergencia
convergencia=y

plt.figure()
plt.subplot(1,2,1)

# plot results (de la convergencia)
for i in range(0,len(x0),2):
        plt.plot(y[:,i],y[:,i+1])
        plt.plot(y[0,i],y[0,i+1], marker=".", color="blue")
        plt.plot(y[-1,i],y[-1,i+1], marker="x", color="red")
        
plt.text(x0[20],x0[21],r'$\xi^{r}$', color='blue')
        
plt.axis([0,2, -0.2, 1.2])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Generación de trayectorias')
plt.grid()
plt.show()


#se genera ahora una lista para las nuevas conidciones iniciales
x02=[]
#Nueva referencia a la que se va a converjer una vez que se forme el circulo y este se desplace
nueva_referencia=[1.8,0.8]


#se añade el ultimo valor de la convergencia del circulo de cada agente, como la nueva condicion inicial y eso se concatena con la lista nueva_referencia
for i in range(len(x0)):
    if i >19:
        x02.append(nueva_referencia[i-20])
    else:
        x02.append(y[-1,i]) #el -1 indica el ultimo valor de la columna
    

#se genera el tiempo en el que se va adesplazar el circulo en linea recta
t2 = np.linspace(0,3.5) 
#se vuelve a llamara al solucionador para que ahora realice el movimiento del circulo en linea recta
y = odeint(model,x02,t2)
#se guarda la trayectoria del desplazamiento horizontal del circulo en la variable desplazamiento 
desplazamiento=y

# plot results (del desplazamiento)
#aqui al tener como condiciones iniciales los ultimos valores de cada agente cuando llego al circulo va a aparentar que es una sola trayectoria
for i in range(0,len(x02),2):
        plt.plot(y[:,i],y[:,i+1])
        plt.plot(y[-1,i],y[-1,i+1], marker="x", color="red")

plt.text(x02[20],x02[21],r'$\xi^{r}$', color='blue')


#se genera una sola trayectoria concatenando las matrices de la variable convergencia y desplazamiento
trayectoria=np.concatenate((convergencia,desplazamiento),axis=0)

#Se concatenan los dos tiempos
t_final=np.concatenate((t,t2),axis=0)

#se grafica toda la trayectoria
plt.subplot(1,2,2)
for i in range(0,len(x0),2):
        plt.plot(trayectoria[:,i],trayectoria[:,i+1])
        plt.plot(trayectoria[0,i],trayectoria[0,i+1], marker=".", color="blue")
        plt.plot(trayectoria[-1,i],trayectoria[-1,i+1], marker="x", color="red")
    
plt.axis([0,2, -0.2, 1.2])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trayectoria final')
plt.grid()
plt.show()





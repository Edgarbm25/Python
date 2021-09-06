import matplotlib.pyplot as plt
import numpy as np


x=np.arange(-5, 40, 0.01)
y1 = np.piecewise(x, [x<0, x>=0,x>=5,x>=10 , x>=15,x>=20], [lambda x: 5, lambda x: x+5, lambda x: 2,lambda x: 10,lambda x: 2,lambda x: 4*np.sin(x)+6])

plt.figure()
plt.plot(x, y1 ,color='red', linestyle = 'dashed', linewidth = '2')

font1 = {'family':'serif','color':'blue','size':10}
font2 = {'family':'serif','color':'orange','size':15}

plt.xlabel("Eje x", fontdict=font1)
plt.ylabel("Eje y",fontdict=font1)
plt.title("Gráfica de prueba",fontdict=font2)
plt.grid(color = 'green', linestyle = '--', linewidth = 1)


plt.show()



import numpy as np

A=np.array([[4,2,3],[1,5,2],[4,8,2]])

x=np.array([1,2,2])

y=np.array([3,5,2])


#---------------------------OPERACIONES--------------------

b=np.matmul(A,x) 

b2=A@x #forma equivalente a b=np.matmul(A,x) 

print("b=",b)

print("b2=",b2)

A_det=np.linalg.det(A) #Determinante 

print("Determinante de A= \n",A_det)

A_inv = np.linalg.inv(A) #Inversa

print("Inversa de A= \n",A_inv)

AT=np.transpose(A) #Transpuesta

print("Transpuesta de A= \n",AT)

x1 = np.linalg.solve(A, b) #Solucionar 

print("x1=",x1)

x2=A_inv@b  #Esto es equivalente a x1 = np.linalg.solve(A, b)

print("x2=",x2)

xdoty=np.dot(x,y) #Producto punto

print("Producto punto de (x,y)=",xdoty)

norm_y=np.linalg.norm(y) #Norma del vector

print("Norma de y=",norm_y)

print("Tamaño de matriz",A.shape) #Ver las dimensiones de la matriz

eigenvalores,eigenvectores = np.linalg.eig(A) #Eigenvectores y eigenvalores 

print("Eigenvalores de A \n = ",eigenvalores)

print("Eigenvectores de A \n = ",eigenvectores) #los da en vector renglon







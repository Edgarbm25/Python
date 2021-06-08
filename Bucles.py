
nombre = 'Edgar'
edad= 25

if nombre == 'Carlos':
      print('Hola Carlos')
elif edad < 20:
    print('Eres muy joven ')
elif  25 < edad :
    print('casi la edad')
else:
    print('no hay datos')

#---------------------Otro ehjemplo con string------------------

name=input('Ingresar nombre')
if name != '':
    print('Gracias por ingresar nombre')
else:
    print('No ingresaste nombre')

#---------------------Ejemplo con while loop------------------

#Este programa declara un string vacio y se repite "ingresa tu nombre" hasta que ingreses Edgar
#Lo que esta dentro del while debe de tener un tabulador, sino marca error
#print('!Gracias¡') ya no esta dentro del while loop

nombre = ''
while nombre != 'Edgar':
      print('Ingresa tu nombre') 
      nombre=input()
print('!Gracias¡') 

#---------------------- Ejemplo While-break----------------------------------------
# #Mismo ejemplo anterior pero con loop infinito

nombre = ''
while True:
      print('Ingresa tu nombre') 
      nombre=input()
      if nombre == 'Edgar':
          break
print('!Gracias¡') 

#----------------------Ejemplo While-continue---------------------------------
#Recordar, todo lo que este dentro de los loop incluyendo los if, debe
#de estar alineado si no no jala

spam=0

while spam<5:
      spam = spam + 1
      if spam==3:
          continue
      print('spam vale'+str(spam))
    
    
#----------------------Ejemplo For loop---------------------------------    
print('Mi nombre es')
for num in range(0,5,1): #(donde empieza,termina,aumento)
    print('Edgar '+ str(num))
    
for num in range(5): #Los parametros de arriba los toma por default si solo se pone de esta manera
    print('Edgar '+ str(num))   


#------------------Otro ejemplo con for--------------------------

letras = ['a','b','c','d']

for i in range(len(letras)):
    print('La casilla ' + str(i) + ' es la letra ' + letras[i] )




























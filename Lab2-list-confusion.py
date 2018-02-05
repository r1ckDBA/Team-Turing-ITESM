#################################
#Team turing
#Lab B.1 Program 2. List confusion
#################################

#importa funcion random para generar cadena de 4 digitos
from random import randint

#Define lista de numeros
#Version normal
#listaUno=[1, 1, 2, 3,33, 5, 8, 13, 21, 34, 55, 89,33]
#listaDos=[1, 2, 3,33, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,33]

#Version extra
listaUno=list(range(0,randint(0,20),randint(1,9)))+list(range(0,randint(0,20),randint(1,9)))+list(range(0,randint(0,20),randint(1,9)))+list(range(0,randint(0,20),randint(1,9)))
listaDos=list(range(0,randint(0,50),randint(1,9)))+list(range(0,randint(0,50),randint(1,9)))+list(range(0,randint(0,20),randint(1,9)))+list(range(0,randint(0,20),randint(1,9)))

print ("ListaUno:"+str(sorted(listaUno)))
print ("ListaDos:"+str(sorted(listaDos)))

listaFinal=[]

for intUno in listaUno:
  if intUno in listaDos:
    #Revisamos que el numero no este repetido
    if intUno not in listaFinal: 
        listaFinal.append(int(intUno))

print("\n-----------\nLista final:"+str(sorted(listaFinal)))
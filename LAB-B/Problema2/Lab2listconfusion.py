#################################
#Team turing
#Lab B.1 Program 2. List confusion
#################################

#importa funcion random para generar cadena de 4 digitos
from random import randint

def comparaListas(listaA, ListaB):
  listaC=[]

  print ("ListaA:"+str(sorted(listaA)))
  print ("ListaB:"+str(sorted(ListaB)))

  for intA in listaA:
    if intA in ListaB:
      #Revisamos que el numero no este repetido
      if intA not in listaC: 
        listaC.append(int(intA))

  return listaC

#Define lista de numeros
#Version normal
#listaUno=[1, 1, 2, 3,33, 5, 8, 13, 21, 34, 55, 89,33]
#listaDos=[1, 2, 3,33, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,33]

#Version extra
listaUno=list(range(0,randint(0,20),randint(1,9)))+list(range(1,randint(0,50),randint(1,9)))+list(range(2,randint(0,20),randint(1,9)))+list(range(0,randint(0,20),randint(1,9)))
listaDos=list(range(0,randint(0,50),randint(1,9)))+list(range(0,randint(0,50),randint(1,9)))+list(range(0,randint(0,20),randint(1,9)))+list(range(0,randint(0,20),randint(1,9)))

listaFinal=comparaListas(listaUno,listaDos)

print("\n-----------\nLista final:"+str(sorted(listaFinal)))
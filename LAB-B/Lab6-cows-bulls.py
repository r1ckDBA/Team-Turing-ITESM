#################################
#Team turing
#Lab B.1 Program 6. cows and bulls
#################################

#importa funcion random para generar cadena de 4 digitos
from random import randint

#Define lista de numeros a adivinar
liSolucion=[]

#Introducimos 4 numeros alearios del 0 al 9
liSolucion.append(randint(0, 9))
liSolucion.append(randint(0, 9))
liSolucion.append(randint(0, 9))
liSolucion.append(randint(0, 9))

#Variable donde almacenamos temporalmente el valor introducido por el usuario
inUsuario=[]

#Numero de turnos que le llevo al usuario adivinar el numero
inTurnos=0

print("\nWelcome to cows and bulls!!")

#Variable con el numero de vacas
inCows=0 

while inCows < 4:
  stUsuario=input('\nIntroduce un numero de 4 digitos:\n>>>> ')
  #convertimos a int
  inUsuario.append(int(stUsuario[0]))
  inUsuario.append(int(stUsuario[1]))
  inUsuario.append(int(stUsuario[2]))
  inUsuario.append(int(stUsuario[3]))

  # Reiniciamos variables con el numero de vacas y toros
  inCows=0 
  inBulls=0

  #Revisamos por vacas y toros
  if inUsuario[0] == liSolucion[0]: inCows=inCows+1
  elif inUsuario[0] == liSolucion[1] or inUsuario[0] == liSolucion[2] or inUsuario[0] == liSolucion[3]: inBulls=inBulls+1

  if inUsuario[1] == liSolucion[1]: inCows=inCows+1
  elif inUsuario[1] == liSolucion[0] or inUsuario[1] == liSolucion[2] or inUsuario[1] == liSolucion[3]: inBulls=inBulls+1

  if inUsuario[2] == liSolucion[2]: inCows=inCows+1
  elif inUsuario[2] == liSolucion[0] or inUsuario[2] == liSolucion[1] or inUsuario[2] == liSolucion[3]: inBulls=inBulls+1

  if inUsuario[3] == liSolucion[3]: inCows=inCows+1
  elif inUsuario[3] == liSolucion[0] or inUsuario[3] == liSolucion[1] or inUsuario[3] == liSolucion[2]: inBulls=inBulls+1
  
  #Limpiamos variable y aumentamos en 1 el numero de turnos que le tomo al usuario encontrar la solucion
  inUsuario[:] = []
  inTurnos=inTurnos+1

  #Imprimimos resultado de la ronda
  print("Tienes "+str(inCows)+" vaca(s)")
  print("Tienes "+str(inBulls)+" toro(s)")

  if inCows == 4: 
    print("\n ------------\n Felicidades!!!! ganaste!!!")  
    print (" Te tomo tan solo "+str(inTurnos)+" turnos")
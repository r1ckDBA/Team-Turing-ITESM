'''
Created on 04/02/2018

@author: juavarga
'''
import sys

def isOddOrEven(num):
    if( (num % 4) == 0 ):
        print(str(num)+" is multiple of four.")
        return (str(num)+" is multiple of four.")
    elif( (num % 2) == 0 ):
        print(str(num)+" is even.")
        return (str(num)+" is even.")
    else :
        print(str(num)+" is odd.")
        return (str(num)+" is odd.")

def checkIsDivisible(num, check):
    if ( (int(num) % int(check)) == 0):
        print(num + " can be divided evenly by " + check)
        return (num + " can be divided evenly by " + check)
    else:
        print(num+ " cannot be divided evenly by " + check)
        return (num+ " cannot be divided evenly by " + check)


#n = input("Write a number : ")
#isOddOrEven(int(n))

#num = input("Write another number : ")
#check = input("Write yet another number to check if it can divide evenly previous number: ")
#checkIsDivisible(num, check)

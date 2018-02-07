'''
Created on 04/02/2018

@author: juavarga
'''

primeNumFile = "One.txt"
primeNumList = ""
with open(primeNumFile) as f:
    primeNumList = f.readlines()
primeNumList = [x.strip() for x in primeNumList]
primeNumList = list(map (int, primeNumList))


happyNumFile = "other.txt"
happyNumList = ""
with open(happyNumFile) as f1:
    happyNumList = f1.readlines()
happyNumList = [x.strip() for x in happyNumList]
happyNumList = list(map (int, happyNumList))

print(primeNumList)
print(happyNumList)

overlapped = []
for num in primeNumList:
    if num in happyNumList:
        overlapped.append(num)

print(overlapped)

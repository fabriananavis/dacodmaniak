"""
password aleatoir
boucle
fonction
"""

import random

chif = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
maj = ["A","B","C","D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "K", "R", "S", "T", "U", "V", "W"," X", "Y", "Z"]
minu = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","y","z"]
cara = ["*","+",";","-",",","/","(",")","[","]"]


longp = random.randint(8,12)
print(longp)

theCara=cara[random.randint(0,9)]
theChif=chif[random.randint(0,8)]
theMinu=minu[random.randint(0,25)]
theMaj=maj[random.randint(0,25)]

oMoin=[theMaj,theCara,theChif]

i=random.randint(0,25)
theMaj=maj[i]
print(theMaj)
    
i=random.randint(0,9)
theCara=cara[i]
print(theCara)

i=random.randint(0,25)
theMinu=minu[i]
print(theMinu)

i=random.randint(0,8)
theChif=chif[i]
print(theChif)



while len(oMoin)< longp:
    boite=random.randint(0,3)
    if boite == 0:
        bigBoite=maj
    if boite == 1:
        bigBoite=minu
    if boite == 2:
        bigBoite=cara
    if boite == 3:
        bigBoite=chif
    ii=random.randint(0,len (bigBoite)-1)
    oMoin.append(bigBoite[ii])
print(oMoin)
random.shuffle(oMoin)
print(oMoin)




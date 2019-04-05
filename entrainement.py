"""
password aleatoir
boucle
fonction
"""



chif = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
maj = ["A","B","C","D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "K", "R", "S", "T", "U", "V", "W"," X", "Y", "Z"]
minu = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","y","z"]
cara = ["*","+",";","-",",","/","(",")","[","]"]
tab = ["chif","maj","minu","cara"]

passw = random.randint(8,12)

for indice in(chif): #pour indice d'un tableau
    
    print (random.randint(0, 9))


    print(random.choice(maj))
  
    print(random.choice(minu))

    print(random.choice(cara))
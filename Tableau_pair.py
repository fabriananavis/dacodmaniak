"""
getLowerOf function
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
        if (firstVal < secondVal):
                return firstVal
        else:
            return secondVal

"""
getGreaterOf function
returns the greater value of two params
"""
def getGreaterOf(firstVal, secondVal):
        if firstVal > secondVal:
                return firstVal
        else:
                return secondVal

"""
compare function
@param firstVal First value to compare
@param secondVal Second value to compare
@param howTo Mode de comparaison souhaité
@return greater of lower value of two depends on how params
""" 
def compare(firstVal, secondVal, desc=True) :
        if (desc):
                return getLowerOf(firstVal, secondVal)
        return getGreaterOf(firstVal, secondVal)

"""
max function
@param anArray The array from wich i want to get the max value
@return the max value of anArray
"""
def max (anArray):
        the = anArray[0]
        for value in anArray(1:)
                theMax = compare(theMax, value, False)
                return theMax
"""
"""

somme = 0
effectif = 0

def moyenne(anArray):
        for val in enumerate(monTableau):
                somme = somme + val
                effectif = effectif + 1
                moyenne = somme / effectif
        return  moyenne    
        
                



#declaration du tableau
monTableau = [3,4,7,12,78,120,250,319]

#
for indice, val in enumerate(monTableau): 
    print(monTableau[indice])


#
for indice, val in enumerate(monTableau):
    if indice %  2 == 0:
        print(monTableau[indice] * 2)





# find a Min solution
MinValue = 9999999
 

mayBeImTheMin = monTableau[0] # Just initialized the min as first time in the array
for val in monTableau[1:]: # Loop over the array from second element
                mayBeImTheMin = getLowerOf(mayBeInTheMin, val)

print("And the min is : ", mayBeImTheMin)



#
mayBeImTheMax = monTableau[0] # Just initialized the min as first time in the array
for val in monTableau[1:]: # Loop over the array from second element
                mayBeImTheMax = getGreaterOf(mayBeInTheMin, val)

print("And the max is : ", mayBeIm[TheMax)

for indice, val in enumerate(monTableau)
moyVal = (val, val)
        return (val + val)

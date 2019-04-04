"""

"""
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
         if val < mayBeImTheMin: # check if the current value in the aarray is lower than the current
                mayBeImTheMin = monTableau[indice]

print("And the min is : ", mayBeImTheMin)



#
mayBeImTheMax = monTableau[0] # Just initialized the min as first time in the array
for val in monTableau[1:]: # Loop over the array from second element
         if val > mayBeImTheMax: # check if the current value in the aarray is lower than the current
                mayBeImTheMax = monTableau[indice]

print("And the max is : ", mayBeImTheMax)

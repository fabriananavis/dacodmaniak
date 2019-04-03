"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest in division

"""

# accept an amount entry
customerSomme=input("Inserez votre billet:")
somme=int(customerSomme)

# Got 100
nbBillet100 = somme // 100
left100 = somme % 100

if left100 > 0:
# Next... Got 50
nbBillet50 = left100 // 50
left50 = left50 % 50

if left50 > 0:
    # Next... Got 20
nbBillet20 = left50 // 20
left20 = left20 % 20

if left20 > 0:
#Next... Got 10
nbBillet10 = left20 // 10
left10 = left10 % 10

if left10 > 0:
    #Next... Got 5
    nbBillet5 = left10 // 5
    left5 = left5 % 5

if left5 > 0:
    #Next.. Got coins2 
    coins2 = somme // 2
    left2 = 
"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest in division

"""
#definition des variables
nbBillet100 = 0 
nbBillet50 = 0
nbBillet20 = 0
nbBillet10 = 0
nbCoins2 = 0
nbCoins1 = 0

#somme due
dueSomme=input("somme à payer")
somme=int(dueSomme)

#somme rendue


#sommes acceptée


# accept an amount entry
customerSomme=input("Inserez votre billet:")
somme=int(customerSomme)

# Got 100
nbBillet100 = somme // 100
left100 = somme % 100

if left100 > 0:
# Next... Got 50
nbBillet50 = left100 // 50
left50 = left100 % 50

if left50 > 0:
    # Next... Got 20
nbBillet20 = left50 // 20
left20 = left50 % 20

if left20 > 0:
#Next... Got 10
nbBillet10 = left20 // 10
left10 = left20 % 10

if left10 > 0:
    #Next... Got 5
    nbBillet5 = left10 // 5
    left5 = left10 % 5



if left5 > 0:
    #Next.. Got 2 
    nbCoins2 = left5 // 5
    left2 = left5 % 2

if left > 0:
    #Next... Got 1
    nbCoins1 = left2 // 2
    left1 = left2 % 2

#Terminé
print("récupérez votre monnaie. Vous avez :", nbBillet100, "billets de 100€,", nbBillet50,"billets de 50€", nbBillet20)
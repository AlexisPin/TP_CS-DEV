
# #Alexis PINCEMIN TP1
# #23/11/2020
# #Exercice 1 
# year = int(input("Entrez l'année:"))
# strYear = str(year)
# def bissextile(year): #fonction qui regarde si l'année est bissextile ou non
#     if year % 4 == 0 and strYear[2] != "0" or strYear[3] != "0" or year % 400 == 0:
       
#        return True
       
#     else:
        
#         return False
        


# mois = input('Quelle mois : ')

# def nombreJour(mois,year): #fonctionne qui donne le jour d'un mois
#     if int(mois) > 12 or int(mois) < 1  :
#         print('mois non valide')
#         mois = int(input('Quelle mois'))
#     elif mois in ["1","3","5","7","8","10","12"]  :  
#         print('Le mois {} comporte 31 jours' .format(mois))
#     elif mois in ["4","6","9","11"] :
#         print('Le mois {} comporte 30 jours' .format(mois))
#     elif mois == "2" and bissextile(year) == True:
#         print('Le mois {} comporte 29 jours' .format(mois))
#     else :
#         print('Le mois {} comporte 28 jours' .format(mois))


# nombreJour(mois,year)

#Exercice 2 
montantTranche1 = 9964
montantTranche2 = 27519
montantTranche3 = 73779
montantTranche4 = 156244
revenu = int(input('Quelle sont vos revenus : '))
def mesImpots(revenu) :
    
    if revenu >= montantTranche4 : 
        impots = (revenu-montantTranche4)*45/100+(montantTranche4-montantTranche3)*41/100+\
        (montantTranche3-montantTranche2)*30/100+(montantTranche2-montantTranche1)*14/100
    elif montantTranche3 <= revenu <= montantTranche4 :
        impots = (revenu-montantTranche3)*41/100+\
        (montantTranche3-montantTranche2)*30/100+(montantTranche2-montantTranche1)*14/100
    elif montantTranche2 <= revenu <= montantTranche3 :
        impots = (revenu-montantTranche2)*30/100+(montantTranche2-montantTranche1)*14/100
    elif montantTranche1 <= revenu <= montantTranche2 :
        impots = (revenu-montantTranche1)*14/100
    return impots

mesImpots(revenu)
print(mesImpots(revenu))

#Exercice 3 
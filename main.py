from entreprise import Entreprice


#############################
    #### Exercice 1 ####
#############################

# Entrepise sans erreur
try:
    entreprise1 = Entreprice("chêne Vert", "avenue de la prairie 34000 Montpellier", "  12345678963214   ")
    print(entreprise1)
    print("Nom de l'entreprise :",entreprise1.name)
    print("Avant modification :", entreprise1.siret)
    entreprise1.siret="36985632156985"
    print("Après modification :", entreprise1.siret)
    
except ValueError as e:
    print(e)

# Entrepise avec erreur
try:
    entreprise2 = Entreprice("Intermarché", "avenue de l'Hortus 34130 Candillargues", "123456")
    print(entreprise2)
except ValueError as e:
    print(e)

#############################

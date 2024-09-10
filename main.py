from entreprise import Entreprice
from connection_data import DatabaseConnection

#############################
    #### Exercice 1 ####
#############################

# # Entrepise sans erreur
# try:
#     entreprise1 = Entreprice("chêne Vert", "avenue de la prairie 34000 Montpellier", "  12345678963214   ")
#     print(entreprise1)
#     print("Nom de l'entreprise :",entreprise1.name)
#     print("Avant modification :", entreprise1.siret)
#     entreprise1.siret="36985632156985"
#     print("Après modification :", entreprise1.siret)
    
# except ValueError as e:
#     print(e)

# # Entrepise avec erreur
# try:
#     entreprise2 = Entreprice("Intermarché", "avenue de l'Hortus 34130 Candillargues", "123456")
#     print(entreprise2)
# except ValueError as e:
#     print(e)


#############################
    #### Exercice 2 ####
#############################


try :
    db1= DatabaseConnection("MySQL", "admin", "9874")
    db2= DatabaseConnection("MySQL", "admin", "9874", "12.269.257.12")
    db3= DatabaseConnection.create_instance_mariadb()
    print(db1)
    print(db2)
    print(db3)
    
    print(DatabaseConnection.get_nbr_instance())
    
except ValueError as e:
    print("Une erreur est survenu")



#############################
    #### Exercice 3 ####
#############################





#############################
    #### Exercice 4 ####
#############################
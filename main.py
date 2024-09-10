from entreprise import Entreprice
from connection_data import DatabaseConnection
from banque import Client, CompteBancaire

#############################
    #### Exercice 1 ####
#############################

# # Entrepise sans erreur
# try:
#     entreprise1 = Entreprice("chêne Vert", "avenue de la prairie 34000 Montpellier", "  12345678963214  ")
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

# try :
#     db1= DatabaseConnection("MySQL", "admin", "9874")
#     db2= DatabaseConnection("MySQL", "admin", "9874", "12.269.257.12")
#     db3= DatabaseConnection.create_instance_mariadb()
#     print(db1)
#     print(db2)
#     print(db3)
    
#     print(DatabaseConnection.get_nbr_instance())
    
# except ValueError as e:
#     print("Une erreur est survenu")


#############################
    #### Exercice 3 ####
#############################

# # Client sans erreur
try:
    # Create clients
    client1 = Client("giac", "vivi", "    123698521478963")
    client2 = Client("Sui", "Ghis", "236985478963258")
    print(client1)
    print(client2)
    
    # Create compte bancaire
    compte1 = CompteBancaire("2024-01-01", client1, 1500.0)
    compte2 = CompteBancaire("2024-04-26", client2, 2600.0)
    compte3 = CompteBancaire("2024-09-05", client1, 600.0)
    compte4 = CompteBancaire("2024-09-05", client2, 600.0)

    # Display Id
    print(compte1.id_interne)
    print(compte2.id_interne)
  
    # Display __eq__
    print(compte4 == compte3)
    
    #display TOTAL_SOLDES
    print(CompteBancaire.total_soldes())
    
except ValueError as e:
    print(e)

# Client avec erreur
# try:
#     client3 = Client("Giacom", "Ange", "    1236211616161616161698521478963")
#     print(client3)

# except ValueError as e:
#     print(e)




#############################
    #### Exercice 4 ####
#############################
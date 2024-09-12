from entreprise import Entreprice
from connection_data import DatabaseConnection
from banque import Client, CompteBancaire
from gestion_movie import Movie


print("\n######################################################")
print("#                                                    #")
print("#    Un grand merci à mon formateur,                 #")
print("#    Robin, pour son aide précieuse !                #")
print("#    Que ce soit par ses cours écrits ou oraux !     #")
print("#    Ce projet n'aurait pas été possible sans        #")
print("#    ses explications claires et son soutien.        #")
print("#                                                    #")
print("######################################################\n")



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

# Client sans erreur
# try:
#     # Create clients
#     client1 = Client("giac", "vivi", "    123698521478963")
#     client2 = Client("Sui", "Ghis", "236985478963258")
#     print(client1)
#     print(client2)
    
#     # Create compte bancaire
#     compte1 = CompteBancaire("2024-01-01", client1, 1500.0)
#     compte2 = CompteBancaire("2024-04-26", client2, 2600.0)
#     compte3 = CompteBancaire("2024-09-05", client1, 600.0)
#     compte4 = CompteBancaire("2024-09-05", client2, 600.0)

#     # Display Id
#     print(compte1.id_interne)
#     print(compte2.id_interne)
  
#     # Display __eq__
#     print(compte4 == compte3)
    
#     #display TOTAL_SOLDES
#     print(CompteBancaire.total_soldes())
    
# except ValueError as e:
#     print(e)

# Client avec erreur
# try:
#     client3 = Client("Giacom", "Ange", "    1236211616161616161698521478963")
#     print(client3)

# except ValueError as e:
#     print(e)


#############################
    #### Exercice 4 ####
#############################

# while True:
#     print("\n==== Menu ====")
#     print("1. Create a new movie")
#     print("2. Read movies (all or by title)")
#     print("3. Update a movie")
#     print("4. Delete a movie")
#     print("5. Exit")
    
#     choice = input("Choose an option (1-5): ")
    
#     if choice == '1':
 
#         title = input("Enter the movie title: ")
#         release_date = input("Enter the release date (DD/MM/YYYY): ")
#         synopsis = input("Enter the movie synopsis: ")
#         movie = Movie(title, release_date, synopsis)
#         movie.dump_movie()
#         print("Movie added successfully!")
    
#     elif choice == '2':

#         sub_choice = input("1. Read all movies\n2. Search by title\nChoose an option: ")
        
#         if sub_choice == '1':
#             print("All movies:")
#             Movie.get_all_movies()
        
#         elif sub_choice == '2':
#             title = input("Enter the movie title: ")
#             movie = Movie.find_movie_by_title(title)
#             if movie:
#                 print(f"Found movie: {movie}")
#             else:
#                 print("Movie not found.")
    
#     elif choice == '3':
#         title = input("Enter the movie title to update: ")
#         movie = Movie.find_movie_by_title(title)
#         if movie:
#             new_title = input("Enter the new title (leave blank to keep unchanged): ")
#             new_release_date = input("Enter the new release date (leave blank to keep unchanged): ")
#             new_synopsis = input("Enter the new synopsis (leave blank to keep unchanged): ")
#             Movie.update_movie(title, new_title=new_title, new_release_date=new_release_date, new_synopsis=new_synopsis)
#         else:
#             print("Movie not found.")
    
#     elif choice == '4':

#         title = input("Enter the movie title to delete: ")
#         Movie.delete_movie(title)
    
#     elif choice == '5':

#         print("Exiting the program.")
#         break
    
#     else:
#         print("Invalid choice. Please choose a valid option.")




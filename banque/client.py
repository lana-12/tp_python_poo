
class Client:
    
    def __init__(self, lastname:str, firstname:str, nir:str ) -> None:
        self.lastname = lastname
        self.firstname = firstname
        self.nir = nir  
        
    
    @property
    def lastname(self)-> str:
        return self.__lastname
    
    @lastname.setter
    def lastname(self, new_lastname: str) -> None:
        self.__lastname = new_lastname.capitalize()
        
    @property
    def firstname(self)-> str:
        return self.__firstname
    
    @firstname.setter
    def firstname(self, new_firstname: str) -> None:
        self.__firstname = new_firstname.capitalize()
        
    @property
    def nir(self)-> str:
        return self.__nir
    
    @nir.setter
    def nir(self, new_nir: str) -> None:
        new_nir = new_nir.strip()
        if len(new_nir) == 15 and new_nir.isdigit():
            self.__nir = new_nir
        else:
            raise ValueError("Erreur dans le numéro de Sécurité Sociale ! Vous devez rentrer 15 chiffres.")

            
        
    def __str__(self) -> str:
        return (f"Nom : {self.lastname}, "
                f"Prénom : {self.firstname}, "
                f"N° NIR : {self.nir}"
                )
    
    
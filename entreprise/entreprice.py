

class Entreprice:
    
    def __init__(self, name: str, address: str, siret: str) -> None:
        self.name = name
        self.address = address
        self.siret = siret
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name.capitalize()
        
    @property
    def address(self) -> str:
        return self.__address
    
    @address.setter
    def address(self, new_address: str) -> None:
        self.__address = new_address.strip()
        
    @property
    def siret(self) -> str:
        return self.__siret
    
    @siret.setter
    def siret(self, new_siret: str) -> None:
        new_siret = new_siret.strip() 
        if len(new_siret) == 14 and new_siret.isdigit():
            self.__siret = new_siret
        else:
            raise ValueError("Erreur dans le numéro de SIRET ! Vous devez rentrer 14 chiffres.")
        
        
        
    def __str__(self) -> str:
        return (f"L'entreprise {self.name} ayant son siège social au {self.address}, possède le numéro de SIRET {self.siret} ")



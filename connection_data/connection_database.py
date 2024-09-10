from dataclasses import dataclass, field

@dataclass
class DatabaseConnection:
    
    
    __database_type: str
    __user: str
    __password: str
    __host: str = field(default="localhost")
    
    NBR_INSTANCE: int = 0
    
    def __post_init__(self):
        DatabaseConnection.NBR_INSTANCE +=1
        
    @staticmethod
    def get_nbr_instance()-> str :
        return f"La classe DatabaseConnection possède actuellement {DatabaseConnection.NBR_INSTANCE} instance(s)."
    
    
    @classmethod
    def create_instance_mariadb(cls):
        return cls("Mariadb", "root", "1234", "76.287.872.12" )
        
    @property
    def database_type(self) -> str:
        return self.__database_type

    @property
    def user(self) -> str:
        return self.__user

    @property
    def password(self) -> str:
        return self.__password

    @property
    def host(self) -> str:
        return self.__host
    
    
    def __str__(self) -> str:
        return (f"Type de connexion : {self.database_type}, "
                f"Hôte : {self.host}, "
                f"User : {self.user}, "
                f"Password : {self.password}, "
                f"Nbr d'instance : {DatabaseConnection.NBR_INSTANCE}"
                )
    
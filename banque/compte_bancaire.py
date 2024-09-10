import random
import string
from datetime import date
from .client import Client


class CompteBancaire:
    
    TOTAL_SOLDES = 0.0 

    def __init__(self, date_creation: str, client: Client, solde: float) -> None:
        self._date_creation = None
        self._id_interne = None
        self._solde = None
        self._client = client

        self.date_creation = date_creation 
        self._generate_id()
        self.solde = solde

    @property
    def date_creation(self):
        return self._date_creation

    @date_creation.setter
    def date_creation(self, value: str):
        try:
            self._date_creation = date.fromisoformat(value)
        except ValueError:
            raise ValueError("La date doit être au format YYYY-MM-DD.")

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, value: float):
        if value < 0:
            raise ValueError("Le solde ne peut pas être négatif.")
        CompteBancaire.TOTAL_SOLDES -= self._solde if self._solde else 0 
        self._solde = value
        CompteBancaire.TOTAL_SOLDES += value

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value: Client):
        if not isinstance(value, Client):
            raise TypeError("Le client doit être une instance de la classe Client.")
        self._client = value


    def _generate_id(self):
        random_letters = ''.join(random.choices(string.ascii_uppercase, k=4))
        formatted_date = self._date_creation.strftime("%d%m%Y")
        self._id_interne = random_letters + formatted_date

    @property
    def id_interne(self):
        return self._id_interne

    @staticmethod
    def total_soldes() -> float:
        return CompteBancaire.TOTAL_SOLDES

    def __eq__(self, other) -> bool:
        return self.solde == other.solde

    def __str__(self) -> str:
        return (f"CompteBancaire(ID: {self.id_interne}, Date: {self.date_creation}, "
                f"Client: {self.client.firstname} {self.client.lastname}, Solde: {self.solde:.2f}€)")


   
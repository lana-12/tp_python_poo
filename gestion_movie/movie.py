import os
import json
import pathlib
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Movie:
    
    __title: str 
    __release_date: str
    __synopsis: str
    
    folder_name: str = "data_json" 
    data_file: ClassVar[pathlib.Path] = pathlib.Path(__file__).parent.joinpath(folder_name, "movies.json")
    
    
    def __post_init__(self):
        folder_path = self.data_file.parent
        if not folder_path.exists():
            print(f"Create folder: {folder_path}")
            folder_path.mkdir(parents=True, exist_ok=True)

        if not self.data_file.exists():
            print(f"Create file json: {self.data_file}")
            data = {"movies": []}  # Utilisation du bon format JSON
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Fichier {self.data_file} créé avec succès.")
        else:
            print(f"File already existing: {self.data_file}")

    @staticmethod
    def load_movies():
        data_file = Movie.data_file 
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and "movies" in data:
                return data["movies"]
            elif isinstance(data, list):
                return data
            else:
                raise ValueError("Le format du fichier JSON est incorrect.")

    @staticmethod
    def save_movies(movies):
        with open(Movie.data_file, 'w', encoding='utf-8') as f:
            json.dump({"movies": movies}, f, ensure_ascii=False, indent=4)
        print("Fichier mis à jour.")

    @staticmethod
    def get_all_movies():
        movies = sorted(Movie.load_movies(), key=lambda x: x['release_date'])
        for movie in movies:
            print(movie)

    @staticmethod
    def find_movie_by_title(title):
        movies = Movie.load_movies()
        title = title.title()
        for movie in movies:
            if movie['title'].title() == title:
                return movie
        return None

    def dump_movie(self):
        """Ajoute le film actuel dans le fichier JSON, s'il n'existe pas déjà."""
        existing_movie = Movie.find_movie_by_title(self.__title)
        if existing_movie:
            print(f"Le film '{self.__title}' existe déjà. Aucun ajout effectué.")
            return
        
        movie_data = {
            "title": self.__title,
            "release_date": self.__release_date,
            "synopsis": self.__synopsis
        }
        movies = Movie.load_movies()
        movies.append(movie_data)
        Movie.save_movies(movies)

    @staticmethod
    def update_movie(title, new_title=None, new_release_date=None, new_synopsis=None):
        movies = Movie.load_movies()
        for movie in movies:
            if movie['title'].title() == title.title():
                if new_title:
                    movie['title'] = new_title.title()
                if new_release_date:
                    movie['release_date'] = new_release_date
                if new_synopsis:
                    movie['synopsis'] = new_synopsis
                Movie.save_movies(movies)
                print(f"Movie '{title}' mis à jour avec success.")
                return
        print(f"Film '{title}' non trouvé.")

    @staticmethod
    def delete_movie(title):
        movies = Movie.load_movies()
        new_movies = [movie for movie in movies if movie['title'].title() != title.title()]
        if len(new_movies) < len(movies):
            Movie.save_movies(new_movies)
            print(f"Film '{title}' supprimé avec succès.")
        else:
            print(f"Film '{title}' non trouvé.")

    def __str__(self):
        return f"Movie(Title: {self.__title}, Release Date: {self.__release_date}, Synopsis: {self.__synopsis})"


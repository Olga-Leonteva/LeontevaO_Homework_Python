import requests
from config_API import Config_API


class Kinopoisk_API:
    def __init__(self):
        self.api_url = Config_API.API_URL
        self.my_headers = {"X-API-KEY": Config_API.API_key}

    def seach_film_by_title(self, new_title):
        response = requests.get(f"{self.api_url}v1.4/movie/search", params={"query": new_title}, headers=self.my_headers)
        response.raise_for_status()
        return response

    def seach_name_person(self, name_person):
        response = requests.get(f"{self.api_url}v1.4/person/search", params={"query": name_person}, headers=self.my_headers)
        response.raise_for_status()
        return response

    def seach_film_person_id(self, person_id):
        response = requests.get(f"{self.api_url}v1.4/movie", params={"persons.id": person_id}, headers=self.my_headers)
        response.raise_for_status()
        return response

    # Негативные проверки
    def seach_wrong_id(self, wrong_id):
        response = requests.get(f"{self.api_url}v1.4/movie", params={"id": wrong_id}, headers=self.my_headers)
        return response

    def seach_wrong_category(self, wrong_category):
        response = requests.get(f"{self.api_url}v1.4/movie", params={"genres.name": wrong_category}, headers=self.my_headers)
        response.raise_for_status()
        return response

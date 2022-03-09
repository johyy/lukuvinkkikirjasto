import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

    def create_user(self, username, password):
        data = {
            "username": username,
            "password": password,
            "password_again": password
        }

        requests.post(f"{self._base_url}/register", data=data)

    # def choose_media(self, data):
    #    data = {"media": data}
    #    requests.post(f"{self._base_url}/choose_media", data=data)

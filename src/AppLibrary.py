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

    def reset_databases(self):
        requests.get(f"{self._base_url}/reset_databases")

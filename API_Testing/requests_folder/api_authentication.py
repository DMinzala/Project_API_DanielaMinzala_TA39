import random

import requests


def generate_token():
    random_number = random.randint(1, 999999999999999999999999999999999999)
    request_body = {
        "clientName": "test_username",
        "clientEmail": f"test_username{random_number}@gmail.com"
    }

    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=request_body)
    return response.json()["accessToken"]
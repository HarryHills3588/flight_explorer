import requests
import json
from dotenv import load_dotenv
import os

class AmadeusClient:
    def __init__(self):
        pass

    def get_access_token():
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": os.getenv("AMADEUS_KEY"),
            "client_secret": os.getenv("AMADEUS_SECRET") 
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(f"API ERROR: COULD NOT GET ACCESS TOKEN | Response: {response}")
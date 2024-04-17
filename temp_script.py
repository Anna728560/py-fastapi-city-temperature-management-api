import os
from datetime import datetime

import requests

from dotenv import load_dotenv

import models

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
LANGUAGE = "en"


def get_weather(city) -> dict:
    response = requests.get(
        BASE_URL,
        params={
            "key": API_KEY,
            "q": city.name,
            "lang": LANGUAGE,
            "units": "metric",
        }
    )
    if response.status_code == 200:
        data = response.json()
        localtime = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]

        date_time = datetime.strptime(localtime, "%Y-%m-%d %H:%M")

        return {
            "date_time": date_time,
            "temperature": temp_c
        }

    else:
        raise ValueError(
            "Something went wrong :c, Please try again with valid data!"
        )


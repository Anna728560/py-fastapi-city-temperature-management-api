import asyncio
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import httpx
import requests

from dotenv import load_dotenv

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
# async def get_weather(city) -> dict:
#     async with httpx.AsyncClient() as client:
#         url = f"{BASE_URL}?key={API_KEY}&q={city.name}&lang={LANGUAGE}&units=metric"
#         response = await client.get(url)
#         print(response)
#
#         if response.status_code == 200:
#             data = await response.json()
#             localtime = data["location"]["localtime"]
#             temp_c = data["current"]["temp_c"]
#
#             date_time = datetime.strptime(localtime, "%Y-%m-%d %H:%M")
#
#             return {
#                 "date_time": date_time,
#                 "temperature": temp_c
#             }
#         else:
#             raise ValueError("Something went wrong :c. Please try again with valid data!")

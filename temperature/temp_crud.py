from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from db import models, database
from temperature import temp_script


def get_all_temperatures(db: Session = Depends(database.get_db)):
    temperatures = db.query(models.Temperature).all()
    return temperatures


def get_one_temperature_by_city_id(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    temperature = db.query(models.Temperature).filter(
        models.Temperature.city_id == city_id
    ).first()

    if not temperature:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City with the id {city_id} does not exist"
        )

    return temperature


def update_all_temperatures(
       db: Session = Depends(database.get_db)
):
    cities = db.query(models.City).all()

    for city in cities:
        try:
            temperature_data = temp_script.get_weather(city)
            temperature = db.query(models.Temperature).filter(
                models.Temperature.city_id == city.id
            ).first()
            if temperature:
                temperature.date_time = temperature_data["date_time"]
                temperature.temperature = temperature_data["temperature"]
            else:
                new_temperature = models.Temperature(
                    city_id=city.id,
                    date_time=temperature_data["date_time"],
                    temperature=temperature_data["temperature"]
                )
                db.add(new_temperature)

        except ValueError as error:
            print(f"Failed to update temperature data for city {city.name}: {str(error)}")
            continue

    db.commit()
    return "Temperature data updated successfully"

# async def update_all_temperatures(
#        db: Session = Depends(database.get_db)
# ):
#     cities = db.query(models.City).all()
#
#     for city in cities:
#         try:
#             temperature_data = await temp_script.get_weather(city)
#             temperature = db.query(models.Temperature).filter(
#                 models.Temperature.city_id == city.id
#             ).first()
#             if temperature:
#                 temperature.date_time = temperature_data["date_time"]
#                 temperature.temperature = temperature_data["temperature"]
#             else:
#                 new_temperature = models.Temperature(
#                     city_id=city.id,
#                     date_time=temperature_data["date_time"],
#                     temperature=temperature_data["temperature"]
#                 )
#                 db.add(new_temperature)
#
#         except ValueError as error:
#             print(f"Failed to update temperature data for city {city.name}: {str(error)}")
#             continue
#
#     db.commit()
#     return "Temperature data updated successfully"

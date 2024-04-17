from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import database



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
        #  api weather logic
        temperature_data = {
            "temperature": 25.5
        }
        new_temperature = models.Temperature(
            city_id=city.id,
            temperature=temperature_data["temperature"]
        )
        db.add(new_temperature)

    db.commit()
    return "Temperature data updated successfully"

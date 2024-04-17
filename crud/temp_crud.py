from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import database
import schemas


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
    return temperature


def update_all_temperatures(
       db: Session = Depends(database.get_db)
):

    return "Temperature data updated successfully"

from typing import List

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

import schemas
import database
from crud.temp_crud import (
    get_all_temperatures,
    get_one_temperature_by_city_id,
    update_all_temperatures,
)


router = APIRouter(
    tags=["Temperatures"],
    prefix="/temperatures"
)


@router.post("/update/")
def update_temperatures(db: Session = Depends(database.get_db)):
    return update_all_temperatures(db=db)


@router.get(
    "/",
    response_model=List[schemas.Temperature]
)
def get_temperatures(db: Session = Depends(database.get_db)):
    return get_all_temperatures(db=db)


@router.get("/{city_id}/")
def get_temperature_by_city(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    return get_one_temperature_by_city_id(city_id=city_id, db=db)


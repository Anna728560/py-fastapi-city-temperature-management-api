from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from db import database
import models
from city import city_schemas


async def create_new_city(
        request: city_schemas.City,
        db: Session = Depends(database.get_db),
):
    db_city = models.City(
        name=request.name,
        additional_info=request.additional_info,
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


async def get_city_by_id(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    city = db.execute(
        select(models.City).filter(models.City.id == city_id)
    ).scalars().first()
    if not city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City with the id {city_id} does not exist"
        )

    return city


async def get_all_cities(db: Session = Depends(database.get_db)):
    cities = db.execute(select(models.City))
    return cities.scalars().all()


async def update_city_by_id(
        city_id: int,
        city: city_schemas.City,
        db: Session = Depends(database.get_db)
):
    db_city = await get_city_by_id(city_id, db)

    for attr, value in city.dict().items():
        setattr(db_city, attr, value)

    db.commit()
    return "Updated"


async def delete_city_by_id(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    db_city = await get_city_by_id(city_id, db)
    db.delete(db_city)
    db.commit()
    return "Deleted"

from fastapi import FastAPI, Depends, status, HTTPException

from sqlalchemy.orm import Session

import models
import schemas
import database
from database import SessionLocal


app = FastAPI()


@app.post("/cities/", status_code=status.HTTP_201_CREATED)
def create_city(
        request: schemas.City,
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


@app.get("/cities/{city_id}/", status_code=status.HTTP_200_OK)
def get_city(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    city = db.query(models.City).filter(models.City.id == city_id).first()
    if not city:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City with the id {city_id} does not exist"
        )

    return city


@app.get("/cities/", status_code=status.HTTP_200_OK)
def get_cities(db: Session = Depends(database.get_db)):
    cities = db.query(models.City).all()
    return cities


@app.put("/cities/{city_id}/", status_code=status.HTTP_202_ACCEPTED)
def update_city(
        city_id: int,
        city: schemas.City,
        db: Session = Depends(database.get_db)
):
    db_city = get_city(city_id, db)

    for attr, value in city.dict().items():
        setattr(db_city, attr, value)

    db.commit()
    return "Updated"

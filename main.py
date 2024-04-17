from fastapi import FastAPI, Depends, status

from sqlalchemy.orm import Session

import schemas
import database
from crud.city_crud import (
    create_new_city,
    get_city_by_id,
    get_all_cities,
    update_city_by_id,
    delete_city_by_id
)


app = FastAPI()


@app.post("/cities/", status_code=status.HTTP_201_CREATED)
def create_city(
        request: schemas.City,
        db: Session = Depends(database.get_db),
):
    return create_new_city(request=request, db=db)


@app.get("/cities/{city_id}/", status_code=status.HTTP_200_OK)
def get_city(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    return get_city_by_id(city_id=city_id, db=db)


@app.get("/cities/", status_code=status.HTTP_200_OK)
def get_cities(db: Session = Depends(database.get_db)):
    return get_all_cities(db=db)


@app.put("/cities/{city_id}/", status_code=status.HTTP_202_ACCEPTED)
def update_city(
        city_id: int,
        city: schemas.City,
        db: Session = Depends(database.get_db)
):
    return update_city_by_id(city_id=city_id, city=city, db=db)


@app.delete("/cities/{city_id}/", status_code=status.HTTP_200_OK)
def delete_city(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    return delete_city_by_id(city_id=city_id, db=db)

from fastapi import FastAPI, Depends, status, HTTPException

from sqlalchemy.orm import Session

from . import models, schemas, database
from database import SessionLocal


app = FastAPI()


@app.get("/cities/", status_code=status.HTTP_201_CREATED)
def create_city(
        request: schemas.CitySchema,
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

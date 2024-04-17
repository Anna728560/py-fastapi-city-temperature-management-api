from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from city import city_schemas
from db import database
from city.city_crud import (
    create_new_city,
    get_city_by_id,
    get_all_cities,
    update_city_by_id,
    delete_city_by_id
)


router = APIRouter(
    tags=["Cities"],
    prefix="/cities"
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_city(
        request: city_schemas.City,
        db: Session = Depends(database.get_db),
):
    return await create_new_city(request=request, db=db)


@router.get(
    "/{city_id}/",
    status_code=status.HTTP_200_OK,
    response_model=city_schemas.CityDetail,
)
async def get_city(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    return await get_city_by_id(city_id=city_id, db=db)


@router.get(
    "/",
    response_model=List[city_schemas.City],
)
async def get_cities(db: Session = Depends(database.get_db)):
    return await get_all_cities(db=db)


@router.put(
    "/{city_id}/",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_city(
        city_id: int,
        city: city_schemas.City,
        db: Session = Depends(database.get_db)
):
    return await update_city_by_id(city_id=city_id, city=city, db=db)


@router.delete(
    "/{city_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_city(
        city_id: int,
        db: Session = Depends(database.get_db)
):
    return await delete_city_by_id(city_id=city_id, db=db)

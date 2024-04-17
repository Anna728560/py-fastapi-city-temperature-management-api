from pydantic import BaseModel

from datetime import datetime


class CityBase(BaseModel):
    name: str
    additional_info: str


class City(CityBase):

    class Config:
        orm_mode = True


# class CityDetail(CityBase):
#     id: int
#     temperature: ""
#
#     class Config:
#         orm_mode = True


class TemperatureBase(BaseModel):
    city_id: int
    date_time: datetime
    temperature: float


class Temperature(TemperatureBase):

    class Config:
        orm_mode = True

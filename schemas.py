from pydantic import BaseModel

from datetime import datetime


class CitySchema(BaseModel):
    id: int
    name: str
    additional_info: str


class TemperatureSchema(BaseModel):
    id: int
    city_id: int
    date_time: datetime
    temperature: float

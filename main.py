from fastapi import FastAPI

import models
from routers import city_routers, temp_routers
import database


app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(city_routers.router)
app.include_router(temp_routers.router)

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def create():
    return {"message": "Hello World"}

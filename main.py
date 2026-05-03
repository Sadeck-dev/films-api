from fastapi import FastAPI
from routes.films import film_router

app = FastAPI()

app.include_router(film_router)
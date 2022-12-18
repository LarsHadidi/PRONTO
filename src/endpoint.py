from fastapi import FastAPI
import database


app = FastAPI()


@app.get("/")
async def root():
    return database.get_location_nodes

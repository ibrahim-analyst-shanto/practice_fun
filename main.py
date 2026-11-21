import os
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
app = FastAPI()

engine = create_engine(os.getenv("DATABASE_URL"))

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

@app.get("/data")
def get_data():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM margetable"))
        data = [dict(row) for row in result.mappings()]
    return {"data": data}


@app.get("/order-details")
def get_data():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM order_details"))
        data = [dict(row) for row in result.mappings()]
    return {"data": data}
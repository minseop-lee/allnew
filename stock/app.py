from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import data
from data import db_conn

app = FastAPI()

db = db_conn()
session = db.sessionmaker()

@app.get('/')
async def healthCheck():
    return "OK"

@app.get('/stock_data')
async def stock_data():
    return data.stock_data()

@app.get('/get_db_data')
async def get_db_data():
    return data.get_db_data()


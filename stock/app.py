from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import data
from data import db_conn
from compound_interest import FutureValueInput, calculate_future_value

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

@app.post('/calculate_future_value')
async def calculate_future_value_endpoint(input_data: FutureValueInput):
    principal = input_data.principal
    interest_rate = input_data.interest_rate
    years = input_data.years
    future_value = calculate_future_value(principal, interest_rate, years)
    return {"years": years, "future_value": future_value}

from fastapi import APIRouter, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
import asyncio
from pydantic import BaseModel
import app.internal.database.db as db
from typing import Dict
from time import sleep

router = APIRouter(
    prefix="/api/v1"
)

class Return(BaseModel):
    data: str

class ReturnID(BaseModel):
    data: int

class DataReception(BaseModel):
    id: int
    full_name: str
    full_name_doctor: str
    date: str
    age: str
    gestational_age: str
    premature: bool
    CLAMS: int
    CAT: int
    GM: int



class DataPerson(BaseModel):
    id: int
    full_name: str
    age: str
    parents_name: str
    address: str
    date_of_visit: str
    specialists_name: str
    meeting_format: str
    personal_factors: str
    neurosurgery: str
    sensitivity: str
    neurourology: str
    mobility: str
    self_service: str
    TCP: str
    neuroorthopedics: str
    coloproctology: str
    productive_activity: str
    leisure: str
    communication: str
    ophthalmology: str
    height_and_weight: str
    smart_functions: str
    pain: str
    tasks: str
    other: str




@router.post("/add_person")
async def add_person(data: DataPerson):
    return {"status": await db.add_new_person(data)}

@router.get("/return_person")
async def return_person(data: Return):
    return {"data": await db.return_person(data.data)}


@router.post("/add_reception")
async def add_reception(data: DataReception):
    return {"status": await db.add_new_reception(data)}

@router.get("/return_reception")
async def return_reception(data: ReturnID):
    return {"data": await db.return_reception(data.data)}
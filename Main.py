from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.crud_database  
collection = db.users  

class User(BaseModel):
    name: str = "Suhaimi"
    email: str = "Suhaimi@sht.gmail.com"
    age: int = 88

def serialize_user(user) -> dict:
    return {"id": str(user["_id"]), "name": user["name"], "email": user["email"], "age": user["age"]}

@app.post("/users/", response_model=dict)
def create_user(user: User):
    new_user = user.dict()
    result = collection.insert_one(new_user)
    return {"id": str(result.inserted_id)}

@app.get("/users/", response_model=List[dict])
def get_users():
    users = collection.find()
    return [serialize_user(user) for user in users]

@app.get("/users/{user_id}", response_model=dict)
def get_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return serialize_user(user)
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=dict)
def update_user(user_id: str, user: User):
    update_result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
    if update_result.modified_count == 1:
        return {"msg": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: str):
    delete_result = collection.delete_one({"_id": ObjectId(user_id)})
    if delete_result.deleted_count == 1:
        return {"msg": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

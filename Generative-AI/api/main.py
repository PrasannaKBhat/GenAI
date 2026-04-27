from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI()

#Mongodb connection
client = AsyncIOMotorClient("mongodb://mongodb:27017")
db = client.demo_db
collection = db.users

class User(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
async def create_user(user: User):
    result = await collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}


@app.get("/users/get")
async def get_users():
    users = []
    async for user in collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

@app.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    await collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.dict()}
    )
    return {"message": "Updated successfully"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    await collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": "Deleted successfully"}
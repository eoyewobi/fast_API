from fastapi import FastAPI, HTTPException
import random
from models import User, Gender, Role, ChangeUser
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
         first_name="Mila",
         last_name="Py",
         gender=Gender.female,
         roles=[Role.user]
         ),
    User(id=uuid4(),
         first_name="James",
         last_name="Jones",
         gender=Gender.male,
         roles=[Role.admin]
         )
]


@app.get('/')
async def root():
    return {'example': 'this is an example', 'data': 100}


@app.get('/api/v1/users')
async def fetch_users():
    return db


@app.post('/api/v1/users')
async def register_users(user: User):
    db.append(user)
    return {"id": user.id}


@app.put('/api/v1/users/{user_id}')
async def update_users(user_update: ChangeUser,user_id: UUID):
    for user in db:
        if user_id == user.id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return f"{user_id} has been updated."
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return f"{user_id} has been removed"
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )


@app.get('/api/v1/random')
async def get_random():
    rn:int = random.randint(0,100)
    return {'number':rn, 'limit': 100}


@app.get('/api/v1/random/{limit}')
async def get_random_limit(limit:int):
    rn:int = random.randint(0,limit)
    return {'number':rn, 'limit': limit}
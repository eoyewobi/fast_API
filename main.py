from fastapi import FastAPI, HTTPException
import random
from models import User, Gender, Role
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
         first_name="Mila",
         last_name="Py",
         gender= Gender.female,
         role= [Role.user]),
    User(id=uuid4(),
         first_name="James",
         last_name="Jones",
         gender= Gender.male,
         role=[Role.admin]
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

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
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
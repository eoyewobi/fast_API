from uuid import uuid4, UUID
from typing import List
import random
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, ChangeUser

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
         first_name="Mila",
         last_name="Py",
         gender=Gender.FEMALE,
         roles=[Role.USER]
         ),
    User(id=uuid4(),
         first_name="James",
         last_name="Jones",
         gender=Gender.MALE,
         roles=[Role.ADMIN]
         )
]


@app.get('/')
async def root():
    """
    set the root page message for the api
    :return:
    """
    return {'example': 'this is an example', 'data': 100}


@app.get('/api/v1/users')
async def fetch_users():
    """
    function to return all users in db
    :return:
    """
    return db


@app.post('/api/v1/users')
async def register_users(user: User):
    """
    function to add users using the api
    :param user:
    :return:
    """
    db.append(user)
    return {"id": user.id}


@app.put('/api/v1/users/{user_id}')
async def update_users(user_update: ChangeUser,user_id: UUID):
    """
    function to update user information using the api
    :param user_update:
    :param user_id:
    :return:
    """
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
    """
    function to delete users using the api
    :param user_id:
    :return:
    """
    users = db.copy()
    for user in users:
        if user.id == user_id:
            db.remove(user)
            return f"{user_id} has been removed"
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )


@app.get('/api/v1/random')
async def get_random():
    """
    function to obtain random numbers using api
    :return:
    """
    random_n:int = random.randint(0,100)
    return {'number':random_n, 'limit': 100}


@app.get('/api/v1/random/{limit}')
async def get_random_limit(limit:int):
    """
    function to get random number and set limit using api
    :param limit:
    :return:
    """
    random_n:int = random.randint(0,limit)
    return {'number':random_n, 'limit': limit}

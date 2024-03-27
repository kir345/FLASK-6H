from typing import List

from fastapi import APIRouter
from db import users, database
from models.user import User, UserIn

router = APIRouter()

@router.post('/users/', response_model=User)
async def create_user(user: UserIn):
    request = users.insert().values(firstname=user.firstname, lastname=user.lastname, email=user.email, password=user.password)
    last_record_id = await database.execute(request)
    return{'user_id': last_record_id}

@router.get('/users/', response_model=List[User])
async def read_users():
    request = users.select()
    return await database.fetch_one(request)

@router.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    request = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(request)

@router.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    request = users.update().where(users.c.usr_id == user_id).values()
    await database.execute(request)
    return {'user_id': user_id}

@router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    request = users.delete().where(users.c.user_id == user_id)
    await database.execute(request)
    return {'mess': 'User delet'}
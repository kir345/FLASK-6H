from typing import List
from sqlalchemy import select
from fastapi import APIRouter
from db import users, products, buyes, database
from models.buy import Buy, BuyIn

router = APIRouter()

@router.post('/buyes/', response_model=Buy)
async def create_buy(buy: BuyIn):
    request = buyes.insert().values(user_id=buy.user_id, product_id= buy.product_id, data=buy.data, status=buy.status)
    last_record_id = await database.execute(request)
    return{'buy_id': last_record_id}

@router.get('/buyes/', response_model=List[Buy])
async def read_buyes():
    request = select(buyes.c.id.label('buy_id'), buyes.c.data.label('data'),
    buyes.c.status.label('status'),
    users.c.id.label('user_id'), users.c.first_name.label('firstname'),
    users.c.last_name.label('lastname'), users.c.email.label('email'),
    products.c.id.label('product_id'), products.c.name.label('name'),
    products.c.description.label('description'), products.c.price.label('price')).join(products).join(users)
    return await database.fetch_one(request)

@router.get('/buyes/{buy_id}', response_model=Buy)
async def read_buy(buy_id: int):
    request = select(buyes.c.id.label('buy_id'), buyes.c.data.label('data'),
    buyes.c.status.label('status'),
    users.c.id.label('user_id'), users.c.first_name.label('firstname'),
    users.c.last_name.label('lastname'), users.c.email.label('email'),
    products.c.id.label('product_id'), products.c.name.label('name'),
    products.c.description.label('description'), products.c.price.label('price')).join(products).join(users)
    return await database.fetch_one(request)

@router.put('/buyes/{buy_id}', response_model=Buy)
async def update_buy(buy_id: int, new_buy: BuyIn):
    request = buyes.update().where(buyes.c.buy_id == buy_id).values(**buy_id.dict())
    await database.execute(request)
    return {'buy_id': buy_id}

@router.delete('/buyes/{buy_id}')
async def delete_buy(buy_id: int):
    request = buyes.delete().where(buyes.c.buy_id == buy_id)
    await database.execute(request)
    return {'mess': 'Buy delet'}
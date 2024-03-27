import datetime
from random import randint, choice
from fastapi import APIRouter
from db import users, products, buyes, database

router = APIRouter()
MIN_PRICE = 1
MAX_PRICE = 50_000

@router.get('/false_data/') 
async def create_note(user_count: int, product_count: int, buy_count: int):
    for i in range(user_count):
        request = users.insert().values(
            firstname=f'firstname_{i}',
            lastname=f'lastname_{i}',
            email= f'mail{i}@m.t',
            password=f'password{i}')
        
        await database.execute(request)

        for i in range(product_count):
            request = products.insert().values(
                name=f'name_{i}',
                description= f'description_{i}',
                price= randint(MIN_PRICE, MAX_PRICE)
            )

        await database.execute(request)

        for i in range(buy_count):
            request = buyes.insert().values(
                user_id= randint(1, user_count),
                product_id = randint(1, product_count),
                data = datetime.date.today(),
                status = choice(['размещен', 'обрабатывается','ожидает оплаты', 'оплачен', 'отправлен', 'доставляется', 'доставлен', 'выполнен', 'отменен'])
            )

            await database.execute(request)
        return{'mess':f'{user_count} false users, {product_count} false products and {buy_count} false buyes created'}
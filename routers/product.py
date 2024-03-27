from typing import List

from fastapi import APIRouter
from db import database, products
from models.product import Product, ProductIn

router = APIRouter()

@router.post('/products/', response_model=Product)
async def create_product(product: ProductIn):
    request = products.insert().values(name=product.name, description=product.description, price=product.price)
    last_record_id = await database.execute(request)
    return{**product.dict(),'product_id': last_record_id}

@router.get('/products/', response_model=List[Product])
async def read_products():
    request = products.select()
    return await database.fetch_one(request)

@router.get('/product/{product_id}', response_model=Product)
async def read_product(product_id: int):
    request = products.select().where(products.c.product_id == product_id)
    return await database.fetch_one(request)

@router.put('/product/{product_id}', response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    request = products.update().where(products.c.product_id == product_id).values()
    await database.execute(request)
    return {'product_id': product_id}

@router.delete('/product/{product_id}')
async def delete_product(product_id: int):
    request = products.delete().where(products.c.product_id == product_id)
    await database.execute(request)
    return {'mess': 'Product delet'}
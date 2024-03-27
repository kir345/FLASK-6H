from fastapi import FastAPI
import uvicorn
from db import database
from routers import user, product, buy, false_data


app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('disconnection')
async def disconnection():
    await database.disconnect()


app.include_router(user.router, tags=['users'])
app.include_router(product.router, tags=['products'])
app.include_router(buy.router, tags=['buy'])
app.include_router(false_data.router, tags=['false_data'])


if __name__ == '__main__':
    uvicorn.run('main_02:app', host='127.0.0.1', port=8000, reload=True)  
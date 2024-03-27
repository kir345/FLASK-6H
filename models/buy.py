import datetime
from enum import Enum
from pydantic import BaseModel, Field, EmailStr

class Status(Enum):
    posted = 'размещен',
    handled = 'обрабатывается',
    awaited = 'ожидает оплаты',
    paid = 'оплачен',
    sented = 'отправлен',
    delivering = 'доставляется',
    delivered = 'доставлен',
    completed = 'выполнен',
    cancelled = 'отменен'


class BuyIn(BaseModel):
    user_id: int = Field(..., name='user_id')
    product_id: int = Field(..., name='product_id')  
    data: datetime.date = Field(..., name='data')
    status: Status = Field(..., name='status')

    class Config:
        use_enum_values = True

class Buy(BuyIn):
    buy_id: int
    firstname: str
    lastname: str
    email: EmailStr
    name: str
    description: str
    price: float

    
    
    
    
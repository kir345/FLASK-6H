from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    name: str = Field(..., name='name', max_length=200)
    description: str = Field(default='', name='description', max_length=500)
    price: float = Field(..., name='price', gt=0, le=50_000)


class Product(ProductIn):
    product_id: int
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    user_id: int
    firstname: str = Field(..., name='first name', max_length=60)
    lastname: str = Field(..., name='last name', max_length= 100)
    email: EmailStr = Field(..., name='email', max_length= 150)

class UserIn(User):
    password: str = Field(..., name = 'password', min_length=8, max_length= 30)
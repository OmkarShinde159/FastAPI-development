from datetime import datetime
from typing import Optional
from pydantic import BaseModel,EmailStr
from pydantic.types import conint

# schema
class PostBase(BaseModel):

    '''created a Post model inherited from BasemModel class to validate the data '''

    title :str
    content : str
    published:bool = True   # added default parameter
    # rating:Optional[int] = None  # added optional parameter


class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime

    class Config:               
        orm_mode = True

# Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, 
# but an ORM model (or any other arbitrary object with attributes).
# id = data["id"]       when data is dict  
# id = data.id          when data is not dict

class Post(PostBase):
    id: int
    created_at : datetime
    owner_id : int
    owner : UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    email : EmailStr
    password : str

class UserLogin(BaseModel):
    email : EmailStr
    password : str 

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


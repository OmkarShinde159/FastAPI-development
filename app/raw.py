


from msilib import schema
from random import randint, randrange
import time
from typing import Optional, List
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from .database import engine, get_db
from .import models,schemas,utils
from .Routers import post,user



models.Base.metadata.create_all(bind=engine)

# FastAPI instance : app

app = FastAPI()



while True:
    try:
        conn = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='123456',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("!!! Database connection was successful !!!")
        break
    except Exception as error:
        print("Connecting to database failed !")
        print("Error: ",error)
        time.sleep(2)

# Creating a list data for performing CRUD operations'
# consider this list as a database
my_posts = [{"title":"Employee Table","content":"name,department","id":1},
{"title":"StreetFood Table","content":"veg, non-veg","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i


app.include_router(post.router)
app.include_router(user.router)





@app.get("/")
def root():

    '''this is a root path'''

    return {"message": "Hello World"}

@app.get("/posts",response_model=List[schemas.Post])
def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts
    # return{"data":posts}

    # cursor.execute("""SELECT*FROM posts""")
    # posts = cursor.fetchall()
    # print(posts) 
    # return {"data":"this is my get post"}

@app.post("/posts",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostBase,db: Session = Depends(get_db)):            # Post is a BaseModel child class 
    # print(post.dict())
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    # return {"data": new_post}


    # cursor.execute('''INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING *''',
    #                     (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    # cursor.execute(f'''INSERT INTO posts (title,content,published)
    #                    VALUES({post.title},{post.content},{post.published})''')   
    # #dont use this in query

    # post_dict = post.dict()    # convert the JSON data into dictionary   
    # post_dict['id'] = randrange(0,100) # create an id key and assign a random number to it
    # my_posts.append(post_dict)     # added the user post into database list
    

    # print(post)             # this data is stored as a pydantic model
    # print(post.dict())      # converted that data into dictionary
    # return {"data": post}   # insert the dictionary in return insted of string
    # print(new_post.title)
    # print(new_post.data)
    # print(new_post.published)
    # print(new_post.rating)
    # print(payLoad)
    # return {"new_post": f"title: {payLoad['title']}, data: {payLoad['data']}"}
    # return {"data":"successfully created post"}


@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int,db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    # print(post)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'post with id:{id} was not found')
    return post
    # return {"post details":post}

    # cursor.execute('''SELECT * FROM posts WHERE id = %s''',(str(id),))
    # post = cursor.fetchone()
    # post = find_post(id)
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {f"message":"Post with id {id} was not found"}

@app.delete("/posts/{id}",status_code=status.HTTP_404_NOT_FOUND)
def delete_posts(id:int, db: Session = Depends(get_db)):
    deleted_post = db.query(models.Post).filter(models.Post.id==id)
    post = deleted_post.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f'post with id:{id} was not found')

    deleted_post.delete(synchronize_session = False)
    db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)

    # cursor.execute('''DELETE FROM posts WHERE id = %s RETURNING*''',(str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    # index = find_index_post(id)
    # my_posts.pop(index)


# update
@app.put("/posts/{id}",response_model=schemas.Post)
def update_post(id: int,updated_post: schemas.PostBase, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id==id)
    
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()                       
    return post_query.first()

    # cursor.execute('''UPDATE posts SET title = %s,content= %s,published= %s WHERE id=%s RETURNING*''',
    #                 (post.title, post.content, post.published,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    # index = find_index_post(id)
    # post_dict = post.dict()
    # post_dict['id'] = id
    # my_posts[index] = post_dict


### for USER end ###
# create a new user and store its id password in db with hash password
@app.post("/users",status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_post(user: schemas.CreateUser,db: Session = Depends(get_db)):

    # hash a password - user password

    hashed_password = utils.hash(user.password)
    user.password = hashed_password


    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# find the user by user id 
@app.get("/users/{id}",response_model=schemas.UserOut)
def get_user(id:int,db: Session = Depends(get_db)):
    '''return the email id of a user'''
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")
                        
    return user
 
from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    email:str
    age: int = None

app = FastAPI()

@app.get("/")
def index():
    return "Hello There!"

# adding path parameters
# paramters in path are called as path parameters
# we can either 
@app.get("/property/{id}")
def property(id:int): #specify the type to prevent user from req wrong type
    return f'This is a property page for id {id}'

@app.post('/user/add/')
def adduser(profile:Profile):
    return {'This is an admin page'}

@app.get('/user/admin')
def admin():
    return {'This is an admin page'}

@app.get("/user/{username}")
def profile(username:str): 
    return f'This is a profile page fir id {username}'

@app.get('/movies')
def movies():
    return {"movies": {"movie1", "movie2"}}

# this route is never reached because there's another similar route above
# ordering matters
# static routes must be placed first
@app.get('/user/admin')
def admin():
    return {'This is an admin page'}

# Query parameters
# url:http://127.0.0.1:8000/products/10?price=100
# Always best to use None as the default value to avoid issues in the url
@app.get('/products/{id}')
def products(id:int, price:float=10):
    return {f'Product with an id: {id} and price {price*id}'}



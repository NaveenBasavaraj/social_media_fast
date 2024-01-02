# Import the FastAPI module
from fastapi import FastAPI, Response, status, HTTPException
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

# Create an instance of the FastAPI application
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{'id': 1, 'title': 'My First Post', 'content': 'This is the content of my first post', 'published': True, 'rating': 5},
             {'id': 2, 'title': 'My Second Post', 'content': 'This is the content of my second post', 'published': True, 'rating': 4}]

# Define a route for the root URL ("/")
@app.get("/")
async def root():
    """
    This function handles the root URL ("/") and returns a JSON response with a message.
    """
    return {"message": "Hello World"}

# Define a route for the "/posts/" URL
@app.get("/posts/")
def get_posts():
    """
    This function handles the "/posts/" URL and returns a JSON response with data.
    """
    return {"data":my_posts}

@app.post("/create/")
def create_posts(payload: dict = Body(...)):
    """
    This function handles the "/create/" URL and creates a new post.
    """
    # You can do whatever you need to do here.
    # Access the payload parameter to get the data from the request.
    return {"message": f"Post created successfully: {payload['title ']} and {payload['content']}"}


@app.post("/createposts/")
def create_posts_pydantic(new_post: Post, response: Response):
    """
    Create a new post using Pydantic model.

    Args:
        new_post (Post): The new post object containing the title, content, and rating.

    Returns:
        dict: A dictionary with a success message and the details of the created post.
    """
    post_dict = new_post.model_dump()
    post_dict['id'] = randrange(3,100)
    my_posts.append(post_dict)
    response.status_code = status.HTTP_201_CREATED
    return {"data": new_post}

@app.get("/posts/latest")
def get_latest_post():
    """
    This function returns the latest post.
    """
    return {"data": my_posts[-1]}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    """
    This function handles the "/posts/{id}" URL and returns a JSON response with data.
    """
    post = [post for post in my_posts if post['id'] == id]
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id {id} not found"}
    return {"data": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    """
    This function deletes a post with the given id.
    """
    post = [post for post in my_posts if post['id'] == id]
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    response.status_code = status.HTTP_204_NO_CONTENT
    my_posts.remove(post[0])
    return {"message": f"Post with id {id} deleted successfully"}
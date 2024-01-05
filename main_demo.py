from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel, Field
from typing import List, Set
from pydantic.networks import HttpUrl


class Profile(BaseModel):
    name: str
    email: str
    age: int = None


class Image(BaseModel):
    url: HttpUrl
    name: str


class Product(BaseModel):
    name: str
    price: float
    discount: int = Field(title="Price of the item", description="Demo description")
    discounted_price: float = None
    tags: Set[str] = set()
    image: List[Image] = []


class Offer(BaseModel):
    name: str
    description: str = None
    price: float
    products: List[Product]


class User(BaseModel):
    name: str
    email: str


app = FastAPI()


@app.post("/addoffer")
def add_offer(offer: Offer):
    return offer


@app.post("/purchase")
def purchase(user: User, product: Product):
    """
    Endpoint to process a purchase.

    Args:
        user (User): The user making the purchase.
        product (Product): The product being purchased.

    Returns:
        dict: A dictionary containing the user and product information.
    """
    return {"user": user, "product": product}


@app.post("/addproduct/{product_id}")
def add_product(product: Product, product_id: int):
    """
    Endpoint to add a product.

    Args:
        product (Product): The product to be added.
        product_id (int): The ID of the product.

    Returns:
        dict: A dictionary containing the product ID and product information.
    """
    product.discounted_price = product.price - (product.price * product.discount) / 100
    return {"product_id": product_id, "product": product}


@app.get("/")
def index():
    """
    Endpoint to return a greeting message.

    Returns:
        str: A greeting message.
    """
    return "Hello There!"


@app.get("/property/{id}")
def property(id: int):
    """
    Endpoint to retrieve property information.

    Args:
        id (int): The ID of the property.

    Returns:
        str: A message indicating the property ID.
    """
    return f"This is a property page for id {id}"


@app.post("/user/add/")
def adduser(profile: Profile):
    """
    Endpoint to add a user.

    Args:
        profile (Profile): The profile of the user to be added.

    Returns:
        dict: A message indicating that the user has been added.
    """
    return {"This is an admin page"}


@app.get("/user/admin")
def admin():
    """
    Endpoint to retrieve admin information.

    Returns:
        dict: A message indicating that this is an admin page.
    """
    return {"This is an admin page"}


@app.get("/user/{username}")
def profile(username: str):
    """
    Endpoint to retrieve user profile information.

    Args:
        username (str): The username of the user.

    Returns:
        str: A message indicating the user profile page for the given username.
    """
    return f"This is a profile page for id {username}"


@app.get("/movies")
def movies():
    """
    Endpoint to retrieve movie information.

    Returns:
        dict: A dictionary containing movie information.
    """
    return {"movies": {"movie1", "movie2"}}


@app.get("/user/admin")
def admin():
    """
    Endpoint to retrieve admin information.

    Returns:
        dict: A message indicating that this is an admin page.
    """
    return {"This is an admin page"}


@app.get("/products/{id}")
def products(id: int, price: float = 10):
    """
    Endpoint to retrieve product information.

    Args:
        id (int): The ID of the product.
        price (float, optional): The price of the product. Defaults to 10.

    Returns:
        dict: A dictionary containing the product ID and calculated price.
    """
    return {f"Product with an id: {id} and price {price*id}"}

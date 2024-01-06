from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: float

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"

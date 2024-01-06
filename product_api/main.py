from fastapi import FastAPI, HTTPException, status, Response
from product_api.schemas import Product
from product_api import models
from product_api.databases import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products")
def prducts(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


@app.get("/product/{id}")
def product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product


@app.delete("product/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(instance=product, synchronize_session=False)
    db.commit()
    return {"message": "Product deleted"}


@app.post("/product")
def add(request: Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name, description=request.description, price=request.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request


@app.put("/product/{id}")
def update(request: Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product_id == id).first()
    if not product.first():
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    product.update(request.model_dump())
    db.commit()
    return {"Product successfully updated"}

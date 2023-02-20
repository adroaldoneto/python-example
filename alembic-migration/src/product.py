from typing import List, Dict
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to PostgreSQL database
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the ORM model for the "products" table
Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)


# Create the FastAPI application
app = FastAPI()


@app.post("/products/")
def create_product(product: Dict):
    try:
        session = SessionLocal()
        product_orm = Product(**product)
        session.add(product_orm)
        session.commit()
        session.refresh(product_orm)
        return product_orm.id
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

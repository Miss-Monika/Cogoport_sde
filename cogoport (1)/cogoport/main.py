# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/create_configuration", response_model=schemas.ConfigurationResponse)
async def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_configuration = await crud.get_configuration(db, country_code=configuration.country_code)
    if db_configuration:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return await crud.create_configuration(db, configuration=configuration)

@app.get("/get_configuration/{country_code}", response_model=schemas.ConfigurationResponse)
async def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = await crud.get_configuration(db, country_code=country_code)
    if not db_configuration:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

@app.post("/update_configuration/{country_code}", response_model=schemas.ConfigurationResponse)
async def update_configuration(country_code: str, configuration: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_configuration = await crud.get_configuration(db, country_code=country_code)
    if not db_configuration:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return await crud.update_configuration(db, country_code=country_code, configuration=configuration)

@app.delete("/delete_configuration/{country_code}", response_model=schemas.ConfigurationResponse)
async def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = await crud.get_configuration(db, country_code=country_code)
    if not db_configuration:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return await crud.delete_configuration(db, country_code=country_code)

# root route should return to the docs
@app.get("/")
async def root():
    return {"message": "Welcome to the Configuration API. Please visit /docs for more information."}
    
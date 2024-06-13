# crud.py
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from .models import CountryConfiguration
from .schemas import ConfigurationCreate, ConfigurationUpdate

async def create_configuration(db: Session, configuration: ConfigurationCreate):
    db_configuration = CountryConfiguration(
        country_code=configuration.country_code,
        configurations=configuration.configurations
    )
    db.add(db_configuration)
    await db.commit()
    await db.refresh(db_configuration)
    return db_configuration

async def get_configuration(db: Session, country_code: str):
    result = await db.execute(select(CountryConfiguration).filter(CountryConfiguration.country_code == country_code))
    return result.scalars().first()

async def update_configuration(db: Session, country_code: str, configuration: ConfigurationUpdate):
    result = await db.execute(select(CountryConfiguration).filter(CountryConfiguration.country_code == country_code))
    db_configuration = result.scalars().first()
    if db_configuration:
        db_configuration.configurations = configuration.configurations
        await db.commit()
        await db.refresh(db_configuration)
        return db_configuration
    return None

async def delete_configuration(db: Session, country_code: str):
    result = await db.execute(select(CountryConfiguration).filter(CountryConfiguration.country_code == country_code))
    db_configuration = result.scalars().first()
    if db_configuration:
        await db.delete(db_configuration)
        await db.commit()
        return db_configuration
    return None

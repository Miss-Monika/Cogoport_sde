# schemas.py
from pydantic import BaseModel, Field
from typing import Dict, Any

class ConfigurationCreate(BaseModel):
    country_code: str = Field(..., example="IN")
    configurations: Dict[str, Any]

class ConfigurationUpdate(BaseModel):
    configurations: Dict[str, Any]

class ConfigurationResponse(BaseModel):
    id: int
    country_code: str
    configurations: Dict[str, Any]

    class Config:
        orm_mode = True

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

# Project schemas
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

# Model schemas
class ModelBase(BaseModel):
    name: str
    file_type: str

class ModelCreate(ModelBase):
    project_id: int

class Model(ModelBase):
    id: int
    file_path: str
    created_at: datetime
    updated_at: datetime
    project_id: int

    class Config:
        orm_mode = True

# Toolpath schemas
class ToolpathBase(BaseModel):
    name: str
    layer_height: float
    infill_density: float

class ToolpathCreate(ToolpathBase):
    project_id: int
    model_id: int

class Toolpath(ToolpathBase):
    id: int
    file_path: str
    created_at: datetime
    updated_at: datetime
    project_id: int
    model_id: int

    class Config:
        orm_mode = True

# Simulation schemas
class SimulationBase(BaseModel):
    name: str

class SimulationCreate(SimulationBase):
    project_id: int
    toolpath_id: int

class Simulation(SimulationBase):
    id: int
    result_path: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: datetime
    project_id: int
    toolpath_id: int

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
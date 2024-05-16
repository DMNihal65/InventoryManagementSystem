from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    UserName: str
    Email: str
    Phone: Optional[str] = None
    Address: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    UserID: int

    class Config:
        orm_mode = True

class ToolBase(BaseModel):
    ToolName: str
    QuantityAvailable: int
    Status: str
    Location: Optional[str] = None

class ToolCreate(ToolBase):
    pass

class ToolUpdate(BaseModel):
    QuantityAvailable: Optional[int] = None
    Status: Optional[str] = None
    Location: Optional[str] = None

    class Config:
        orm_mode = True

class Tool(ToolBase):
    ToolID: int
    LastUpdated: Optional[datetime]

    class Config:
        orm_mode = True

class ToolRequestBase(BaseModel):
    UserID: int
    ToolID: int
    QuantityNeeded: int
    PurposeOfUse: str
    AdditionalComments: Optional[str] = None
    RequestDate: Optional[datetime] = None
    Status: Optional[str] = 'Pending'
    AdminID: Optional[int] = None
    AdminApprovalDate: Optional[datetime] = None

class ToolRequestCreate(ToolRequestBase):
    pass

class ToolRequestUpdate(BaseModel):
    QuantityNeeded: Optional[int] = None
    PurposeOfUse: Optional[str] = None
    AdditionalComments: Optional[str] = None
    Status: Optional[str] = None
    AdminID: Optional[int] = None
    AdminApprovalDate: Optional[datetime] = None

    class Config:
        orm_mode = True

class ToolRequest(ToolRequestBase):
    RequestID: int

    class Config:
        orm_mode = True

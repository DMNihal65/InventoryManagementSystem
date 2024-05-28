from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DepartmentBase(BaseModel):
    Name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    DepID: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    UserName: str
    Email: str
    Phone: str
    Address: str
    DepartmentID: int

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

class RequestDetail(BaseModel):
    RequestID: int
    UserID: int
    UserName: str
    ToolID: int
    ToolName: str
    QuantityNeeded: int
    PurposeOfUse: str
    AdditionalComments: Optional[str]
    RequestDate: datetime
    Status: str

    class Config:
        orm_mode = True

class InventoryAnalytics(BaseModel):
    total_tools: int
    total_requests: int
    pending_requests: int
    approved_requests: int
    rejected_requests: int
    tools_in_use: int
    tools_available: int

    class Config:
        orm_mode = True

class MonthlyToolRequests(BaseModel):
    month: str
    total_requests: int

    class Config:
        orm_mode = True

class ToolRequestStatusDistribution(BaseModel):
    status: str
    count: int

    class Config:
        orm_mode = True

class ToolAvailabilityAndUsage(BaseModel):
    available: int
    in_use: int

    class Config:
        orm_mode = True

class RequestsByDepartment(BaseModel):
    department_name: str
    status: str
    count: int

    class Config:
        orm_mode = True

class MostRequestedTools(BaseModel):
    tool_name: str
    request_count: int

    class Config:
        orm_mode = True

class ToolsInUseTrends(BaseModel):
    month: str
    tools_in_use: int

    class Config:
        orm_mode = True

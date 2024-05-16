from sqlalchemy import Column, ForeignKey, Integer, String, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database.database import Base


class User(Base):
    __tablename__ = "users"
    UserID = Column(Integer, primary_key=True, index=True)
    UserName = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Phone = Column(String)
    Address = Column(String)

    # Relationship with ToolRequest
    requests = relationship("ToolRequest", back_populates="user")


class Tool(Base):
    __tablename__ = "tools"
    ToolID = Column(Integer, primary_key=True, index=True)
    ToolName = Column(String, nullable=False)
    QuantityAvailable = Column(Integer, nullable=False)
    Status = Column(Enum('Available', 'In Use', name='tool_status_enum'), nullable=False)
    Location = Column(String)
    LastUpdated = Column(TIMESTAMP)

    # Relationship with ToolRequest
    requests = relationship("ToolRequest", back_populates="tool")


class ToolRequest(Base):
    __tablename__ = "tool_requests"
    RequestID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.UserID"))  # Corrected column name
    ToolID = Column(Integer, ForeignKey("tools.ToolID"))  # Corrected column name
    QuantityNeeded = Column(Integer, nullable=False)
    PurposeOfUse = Column(String)
    AdditionalComments = Column(String)
    RequestDate = Column(TIMESTAMP)
    Status = Column(Enum('Pending', 'Approved', 'Rejected', name='request_status_enum'), default='Pending')
    AdminID = Column(Integer)
    AdminApprovalDate = Column(TIMESTAMP)

    # Relationships
    user = relationship("User", back_populates="requests")
    tool = relationship("Tool", back_populates="requests")

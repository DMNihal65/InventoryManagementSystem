from sqlalchemy.orm import Session
from app.models.models import ToolRequest
from app.schemas.schemas import ToolRequestCreate, ToolRequestUpdate

def get_tool_request(db: Session, request_id: int):
    return db.query(ToolRequest).filter(ToolRequest.RequestID == request_id).first()

def create_tool_request(db: Session, tool_request: ToolRequestCreate):
    db_tool_request = ToolRequest(**tool_request.dict())
    db.add(db_tool_request)
    db.commit()
    db.refresh(db_tool_request)
    return db_tool_request

def update_tool_request(db: Session, request_id: int, tool_request_update: ToolRequestUpdate):
    db_tool_request = db.query(ToolRequest).filter(ToolRequest.RequestID == request_id).first()
    for key, value in tool_request_update.dict(exclude_unset=True).items():
        setattr(db_tool_request, key, value)
    db.commit()
    db.refresh(db_tool_request)
    return db_tool_request

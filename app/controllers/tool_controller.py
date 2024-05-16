from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, get_db
from app.schemas.schemas import ToolCreate, ToolUpdate, Tool
from ..curd.tool_crud import get_tool, create_tool, update_tool

router = APIRouter()

@router.get("/tools/{tool_id}", response_model=Tool)
def read_tool(tool_id: int, db: Session = Depends(get_db)):
    tool = get_tool(db, tool_id=tool_id)
    if tool is None:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool

@router.post("/tools/", response_model=Tool)
def create_new_tool(tool: ToolCreate, db: Session = Depends(get_db)):
    return create_tool(db=db, tool=tool)

@router.put("/tools/{tool_id}", response_model=Tool)
def update_existing_tool(tool_id: int, tool_update: ToolUpdate, db: Session = Depends(get_db)):
    return update_tool(db=db, tool_id=tool_id, tool_update=tool_update)
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.curd.tool_crud import update_tool
from app.database.database import SessionLocal, get_db
from app.schemas.schemas import ToolRequestCreate, ToolRequestUpdate, ToolRequest, ToolUpdate
from ..curd.tool_request_crud import get_tool_request, create_tool_request, update_tool_request

router = APIRouter()

@router.get("/tool_requests/{request_id}", response_model=ToolRequest)
def read_tool_request(request_id: int, db: Session = Depends(get_db)):
    request = get_tool_request(db, request_id=request_id)
    if request is None:
        raise HTTPException(status_code=404, detail="Request not found")
    return request

@router.post("/tool_requests/", response_model=ToolRequest)
def create_new_tool_request(tool_request: ToolRequestCreate, db: Session = Depends(get_db)):
    return create_tool_request(db=db, tool_request=tool_request)

@router.put("/tool_requests/{request_id}", response_model=ToolRequest)
def update_existing_tool_request(request_id: int, tool_request_update: ToolRequestUpdate, db: Session = Depends(get_db)):
    return update_tool_request(db=db, request_id=request_id, tool_request_update=tool_request_update)


@router.put("/tool_requests/{request_id}/approve", response_model=ToolRequest)
def approve_tool_request(request_id: int, db: Session = Depends(get_db)):
    request = get_tool_request(db, request_id=request_id)
    if request is None:
        raise HTTPException(status_code=404, detail="Request not found")

    if request.Status != 'Pending':
        raise HTTPException(status_code=400, detail="Request is not pending for approval")

    # Update request status to 'Approved'
    request_update_data = ToolRequestUpdate(Status='Approved', AdminID=1, AdminApprovalDate=datetime.now())
    request = update_tool_request(db=db, request_id=request_id, tool_request_update=request_update_data)

    # Update tool status to 'In Use' and reduce quantity available
    tool_update_data = ToolUpdate(Status='In Use', QuantityAvailable=request.QuantityNeeded)
    tool = update_tool(db=db, tool_id=request.ToolID, tool_update=tool_update_data)

    return request
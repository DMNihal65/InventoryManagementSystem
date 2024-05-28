from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, get_db
from app.schemas.schemas import InventoryAnalytics, \
     MonthlyToolRequests, ToolRequestStatusDistribution
from ..curd.inventory_crud import get_inventory_analytics, \
    get_tool_request_status_distribution, get_monthly_tool_request_trends

router = APIRouter()

@router.get("/inventory/analytics", response_model=InventoryAnalytics)
def get_inventory_stats(db: Session = Depends(get_db)):
    return get_inventory_analytics(db)





@router.get("/analytics/monthly_tool_request_trends", response_model=List[MonthlyToolRequests])
def get_monthly_tool_requests_trends(db: Session = Depends(get_db)):
    monthly_tool_requests = get_monthly_tool_request_trends(db)
    return monthly_tool_requests


@router.get("/analytics/tool_request_status_distribution", response_model=List[ToolRequestStatusDistribution])
def get_tool_request_status_dist(db: Session = Depends(get_db)):
    return get_tool_request_status_distribution(db)



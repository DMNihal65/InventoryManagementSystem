from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.models import Department, Tool, ToolRequest, InventoryAnalytics
from app.schemas.schemas import ToolRequestStatusDistribution


def get_inventory_analytics(db: Session) -> InventoryAnalytics:
    total_tools = db.query(func.count(Tool.ToolID)).scalar()
    total_requests = db.query(func.count(ToolRequest.RequestID)).scalar()
    pending_requests = db.query(func.count(ToolRequest.RequestID)).filter(ToolRequest.Status == 'Pending').scalar()
    approved_requests = db.query(func.count(ToolRequest.RequestID)).filter(ToolRequest.Status == 'Approved').scalar()
    rejected_requests = db.query(func.count(ToolRequest.RequestID)).filter(ToolRequest.Status == 'Rejected').scalar()
    tools_in_use = db.query(func.sum(Tool.QuantityAvailable)).filter(Tool.Status == 'In Use').scalar() or 0
    tools_available = db.query(func.sum(Tool.QuantityAvailable)).filter(Tool.Status == 'Available').scalar() or 0

    return InventoryAnalytics(
        total_tools=total_tools,
        total_requests=total_requests,
        pending_requests=pending_requests,
        approved_requests=approved_requests,
        rejected_requests=rejected_requests,
        tools_in_use=tools_in_use,
        tools_available=tools_available
    )




def get_monthly_tool_request_trends(db: Session):
    monthly_requests = db.query(func.date_trunc('month', ToolRequest.RequestDate).label("month"), func.count(ToolRequest.RequestID)).group_by("month").all()
    monthly_tool_requests = [{"month": month.strftime("%Y-%m"), "total_requests": count} for month, count in monthly_requests]
    return monthly_tool_requests


def get_tool_request_status_distribution(db: Session) -> List[ToolRequestStatusDistribution]:
    status_distribution = db.query(ToolRequest.Status, func.count(ToolRequest.RequestID)).group_by(ToolRequest.Status).all()
    return [{"status": status, "count": count} for status, count in status_distribution]



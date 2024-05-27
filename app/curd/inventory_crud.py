from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.models import Tool, ToolRequest, InventoryAnalytics


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

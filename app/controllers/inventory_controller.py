from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, get_db
from app.schemas.schemas import InventoryAnalytics
from ..curd.inventory_crud import get_inventory_analytics

router = APIRouter()

@router.get("/inventory/analytics", response_model=InventoryAnalytics)
def get_inventory_stats(db: Session = Depends(get_db)):
    return get_inventory_analytics(db)



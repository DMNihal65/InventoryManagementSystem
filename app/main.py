from fastapi import FastAPI
from app.controllers import user_controller, tool_controller, tool_request_controller
from app.database.database import engine
from app.models.models import Base

app = FastAPI()


# Drop existing tables if needed
# Base.metadata.drop_all(bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)



Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router)
app.include_router(tool_controller.router)
app.include_router(tool_request_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="172.18.7.27", port=8000)
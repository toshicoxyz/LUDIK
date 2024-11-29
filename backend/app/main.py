from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.task_routes import router as taskRouter
from app.config.connection import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="API for managing tasks with CRUD operations",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(taskRouter, prefix="/api/tasks", tags=["Tasks"])

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8011, reload=True)

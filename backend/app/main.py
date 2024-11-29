from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.task_routes import router as taskRouter
from app.config.connection import engine, Base
from .middleware.middleware import ContentSecurityPolicyMiddleware

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

# csp_policy = (
#     "default-src 'self'; "
#     "img-src 'self' data: http://localhost:3000; "  # Permitir las imágenes de fastapi.tiangolo.com
#     "script-src 'self' https://localhost:3000; "  # Permitir los scripts de jsdelivr
#     "style-src 'self' 'unsafe-inline' https://localhost:3000; "  # Permitir los estilos de jsdelivr
#     "font-src 'self' https://localhost:3000;"  # Permitir las fuentes de jsdelivr
# )

# app.add_middleware(ContentSecurityPolicyMiddleware, policy=csp_policy)
app.include_router(taskRouter, prefix="/api/tasks", tags=["Tasks"])

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8011, reload=True)

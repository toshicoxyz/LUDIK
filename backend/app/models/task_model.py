from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
from app.config.connection import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum("Pendiente", "En Proceso", "Completada", name="task_status"), default="Pendiente")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

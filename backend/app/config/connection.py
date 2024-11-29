from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
import logging
from typing import Generator
from dotenv import load_dotenv
import os

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("DatabaseConnection")

# Cargar variables de entorno
load_dotenv()

# Leer las variables desde el entorno
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DB_NAME")

# Loggear las variables de entorno para depuración
logger.info("Variables de entorno cargadas:")
logger.info(f"USER: {USER}")
logger.info(f"PASSWORD: {'*' * len(PASSWORD) if PASSWORD else None}")  # No imprimir la contraseña directamente
logger.info(f"HOST: {HOST}")
logger.info(f"PORT: {PORT}")
logger.info(f"DATABASE: {DATABASE}")

# Construir la URL de conexión para PostgreSQL
if PORT:
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
else:
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

# Loguear la URL de conexión (en modo debug)
logger.debug(f"URL de conexión: {DATABASE_URL}")

if not DATABASE_URL:
    logger.error("DATABASE_URL no está definida en las variables de entorno.")
    raise ValueError("La URL de conexión a la base de datos no está definida.")

logger.info(f"Intentando conectar a la base de datos en: {DATABASE_URL}")

# Crear el motor de SQLAlchemy
try:
    engine = create_engine(DATABASE_URL, echo=True)  # `echo=True` muestra las consultas SQL ejecutadas
    logger.info("Motor de SQLAlchemy creado exitosamente.")
except SQLAlchemyError as e:
    logger.error(f"Error al crear el motor de SQLAlchemy: {str(e)}")
    raise

# Crear la base declarativa y la fábrica de sesiones
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener una sesión de base de datos
def get_db() -> Generator[Session, None, None]:
    logger.info("Obteniendo una nueva sesión de base de datos...")
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        logger.error(f"Error durante la operación de la base de datos: {str(e)}")
        raise
    finally:
        logger.info("Cerrando la sesión de base de datos...")
        db.close()

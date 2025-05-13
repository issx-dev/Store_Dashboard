# LIBRARIES
from decouple import config

# ENV VARIABLES
MONGO_CONECTION_URL = config("MONGO_CONECTION_URL", cast=str)
DATABASE_NAME = config("DATABASE_NAME", cast=str)

if not MONGO_CONECTION_URL and DATABASE_NAME:
    raise ValueError(
        "Las variables de entorno deben de estar correctamente configuradas"
    )

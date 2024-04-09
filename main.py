from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from src.config.db import Database
from src.services.api_router_services import API_ROUTER
import src.services.cors_services as cors_services
from src.helpers.my_loger_herlper import MyLogger
app = FastAPI(title="Api conectada a PostgreSQL", version="v1.0.00")

cors_services.set_cors(app)
app.include_router(API_ROUTER)

try:
    db = Database()
    MyLogger.green("Conexión a la base de datos exitosa.")
except psycopg2.OperationalError as e:
    MyLogger.red(f"Error al conectar a la base de datos: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

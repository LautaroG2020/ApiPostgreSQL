from fastapi import APIRouter
import src.routes.user_routes as user_routes

API_ROUTER = APIRouter(prefix="/v1")

user_routes.add_routes(API_ROUTER)
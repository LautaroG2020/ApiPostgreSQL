from fastapi import APIRouter
import src.controllers.user_controller as controller
from src.models.classes.user_records import NewUserRequest

def add_routes(API_ROUTER: APIRouter):
    @API_ROUTER.get("/users", status_code=200, description="Obtener todos los usuarios", tags=["Usuarios"])
    def get_all_users():
        return controller.get_all_users()

    @API_ROUTER.post("/new-user", status_code=201, description="Insertar un nuevo usuario", tags=["Usuarios"])
    def create_user(user: NewUserRequest):
        result = controller.create_user(user)

        if result == 0:
            return {"message": "No se pudo insertar el usuario"}
        
        return {"message": "Usuario insertado exitosamente"}

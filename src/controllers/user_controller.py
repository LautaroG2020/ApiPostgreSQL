from src.models.classes.user_records import NewUserRequest
import src.models.user_models as UserModel

user_model = UserModel.UserModel()

def get_all_users():
    return user_model.get_all_users()

def create_user(user: NewUserRequest):
    return user_model.create_user(user)
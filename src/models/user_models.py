from src.config.db import Database
from src.models.classes.user_records import NewUserRequest 

class UserModel:
    def __init__(self):
        self.db = Database()

    def get_all_users(self):
        query = "SELECT * FROM Users"
        self.db.cursor.execute(query)
        users = self.db.cursor.fetchall()
        return [NewUserRequest(user_id=user[0], user_name=user[1], user_email=user[2], user_password=user[3]) for user in users]

    def get_user_by_id(self, user_id: int):
        query = f"SELECT * FROM Users WHERE id = {user_id}"
        self.db.cursor.execute(query)
        user = self.db.cursor.fetchone()
        if user:
            return NewUserRequest(user_id=user[0], user_name=user[1], user_email=user[2], user_password=user[3])
        else:
            return None

    def create_user(self, user: NewUserRequest):
        query = f"INSERT INTO Users (name, email, password) VALUES ('{user.user_name}', '{user.user_email}', '{user.user_password}')"
        self.db.cursor.execute(query)
        self.db.conn.commit()
        return self.db.cursor.rowcount

    def update_user(self, user_id, user):
        query = f"UPDATE Users SET name = '{user.user_name}', email = '{user.user_email}', password = '{user.user_password}' WHERE id = {user_id}"
        self.db.cursor.execute(query)
        self.db.conn.commit()
        return self.db.cursor.rowcount

    def delete_user(self, user_id):
        query = f"DELETE FROM Users WHERE id = {user_id}"
        self.db.cursor.execute(query)
        self.db.conn.commit()
        return self.db.cursor.rowcount
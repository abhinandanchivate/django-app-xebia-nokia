# services for user management
from apps.users.models import User
from apps.users.repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    def create_user(self, data):
        """
        Create a new user with the provided data.
        """
        return self.user_repository.create_user(data)
    def get_user_by_id(self, user_id):
        """
        Fetch a user by their ID.
        """
        return self.user_repository.get_user_by_id(user_id)
    def get_all_users(self):
        """
        Fetch all users.
        """
        return self.user_repository.get_all_users()
    def user_exists(self, user_id):
        """
        Check if a user exists by their ID.
        """
        return self.user_repository.user_exists(user_id)
    def delete_user(self, user_id):
        """
        Delete a user by their ID.
        """
        return self.user_repository.delete_user(user_id)
    def update_user(self, user_id, data):
        """
        Update a user's information.
        """
        return self.user_repository.update_user(user_id, data)
    def authenticate_user(self, username, password):
        """
        Authenticate a user with the provided username and password.
        """
        return self.user_repository.authenticate_user(username, password)
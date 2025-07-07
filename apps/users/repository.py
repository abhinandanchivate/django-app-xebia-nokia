# # should hanlde all db related operations for the users app
# # repo for users app
# # repository should handle the db realted operations for role part.

# from apps.roles.models import Role
# # only 1 ==> just to call the method ==> only 1 
# # restrict code to generate only 1 object
# # generic problem ==> design pattern ==> gettign one obkject
# # singleton 
# class RoleRepository:
#     def create_role(self,data):
#         """
#         List of business constraints : 
#         1. Role name should be unique.
#         2. Level should be a positive integer.
#         3. Permissions should be a json object(req) permission values must be a boolean.
#         4. Description should be optional.

#         """
#         role = Role.objects.create(**data)
#         return role
#     def get_role_by_id(self, role_id):
#         """
#         Fetch a role by its ID.
#         """
       
#         return Role.objects.get(id=role_id)
    
#     def get_all_roles(self):
#         """
#         Fetch all roles.
#         """
#         return Role.objects.all()
    
#     # role exists or not
#     def role_exists(self, role_id):
#         """
#         Check if a role exists by its ID.
#         """
#         return Role.objects.filter(id=role_id).exists()
    
#     # delete user
#     def delete_role(self, role_id):
#         """
#         Delete a role by its ID.
#         """
#         role = self.get_role_by_id(role_id)
#         role.delete()
#         return True
        
from apps.users.models import Users
class UserRepository:
    def create_user(self, data):
        """
        Create a new user with the provided data.
        """
        
        user = Users.objects.create(**data)
        return user
    def get_user_by_id(self, user_id):
        """
        Fetch a user by their ID.
        """
        return Users.objects.get(id=user_id)
    def get_all_users(self):
        """
        Fetch all users.
        """
        return Users.objects.all()
    def user_exists(self, user_id):
        """
        Check if a user exists by their ID.
        """
        return Users.objects.filter(id=user_id).exists()
    def delete_user(self, user_id):
        """
        Delete a user by their ID.
        """
        user = self.get_user_by_id(user_id)
        user.delete()
        return True
    def update_user(self, user_id, data):
        """
        Update a user's information.
        """
        user = self.get_user_by_id(user_id)
        for attr, value in data.items():
            setattr(user, attr, value)
        user.save()
        return user
    def authenticate_user(self, username, password):
        """
        Authenticate a user with the provided username and password.
        """
        try:
            user = Users.objects.get(username=username)
            if user.password == password:  # In practice, use hashed passwords
                return user
            else:
                return None
        except Users.DoesNotExist:
            return None

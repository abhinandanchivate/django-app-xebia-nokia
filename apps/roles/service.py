# we may have other service integrations or rest api calls.
# django : does not have direct facility of DI 
# 1. manage it manually
# 2. use django injector(lib name)
from injector import inject
from apps.roles.repository import RoleRepository 
class RoleService:
    @inject
    # to bring the role_repository into the service class

    def __init__(self, user_service, role_repository:RoleRepository):
        self.role_repository = role_repository

   
    def create_role(self,data):
        # here we need to use the repo object ? 

        return self.role_repository.create_role(data)
    def get_all_roles(self):
        return self.role_repository.get_all_roles()
    def get_role_by_id(self, role_id):
        return self.role_repository.get_role_by_id(role_id)
    def role_exists(self, role_id):
        return self.role_repository.role_exists(role_id)
    def delete_role(self, role_id):
        return self.role_repository.delete_role(role_id)
    
        """
        List of business constraints : 
        1. Role name should be unique.
        2. Level should be a positive integer.
        3. Permissions should be a json object(req) permission values must be a boolean.
        4. Description should be optional.

        """
        
    def get_role_by_id(self, role_id):
        """
        Fetch a role by its ID.
        """
       
        return Role.objects.get(id=role_id)
    
    def get_all_roles(self):
        """
        Fetch all roles.
        """
        return Role.objects.all()
    
    # role exists or not
    def role_exists(self, role_id):
        """
        Check if a role exists by its ID.
        """
        return Role.objects.filter(id=role_id).exists()
    
    # delete user
    def delete_role(self, role_id):
        """
        Delete a role by its ID.
        """
        role = self.get_role_by_id(role_id)
        role.delete()
        return True
    
    def update_role(self, role_id, data):
        """
        Update a role by its ID.
        """
        if not self.role_exists(role_id):
            raise ValueError("Role does not exist")
        
        role = self.get_role_by_id(role_id)
        for key, value in data.items():
            setattr(role, key, value)
        role.save()
        return role
        
   
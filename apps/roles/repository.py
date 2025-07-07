# repository should handle the db realted operations for role part.

from apps.roles.models import Role
# only 1 ==> just to call the method ==> only 1 
# restrict code to generate only 1 object
# generic problem ==> design pattern ==> gettign one obkject
# singleton 
class RoleRepository:
    def create_role(self,data):
        """
        List of business constraints : 
        1. Role name should be unique.
        2. Level should be a positive integer.
        3. Permissions should be a json object(req) permission values must be a boolean.
        4. Description should be optional.

        """
        role = Role.objects.create(**data)
        return role
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
        
        

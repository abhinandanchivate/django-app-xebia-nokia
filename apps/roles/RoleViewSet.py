from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from injector import inject
from apps.roles.service import RoleService
from apps.roles.serializers import RoleSerializer
class RoleViewSet(ViewSet):
    @inject
    def __init__(self, role_service:RoleService):
        """
        Initialize the RoleViewSet with the RoleService.
        """
        self.role_service = role_service
    def create(self, request:Request):
        """
        Create a new role.
        
          List of business constraints : 
        1. Role name should be unique.
        2. Level should be a positive integer.
        3. Permissions should be a json object(req) permission values must be a boolean.
        4. Description should be optional.
        5. validate the data 
        """
        data = request.data
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
           role = self.role_service.create_role (data)
           return Response({"role": role}, status=201)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
    def list(self, request:Request):
        """
        List all roles.
        if not available then return no data found 
        """
        roles = self.role_service.get_all_roles()
        if roles:
            serializer = RoleSerializer(roles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No data found"}, status=status.HTTP_404_NOT_FOUND)
        
    def retrieve(self, request:Request, pk=None):
        """
        Get a role by id.
        """
        if not pk:
            return Response({"message": "Role ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        role = self.role_service.get_role_by_id(pk)
        if role:
            serializer = RoleSerializer(role)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
    def destroy(self, request:Request, pk=None):
        """
        Delete a role by id.
        """
        if not pk:
            return Response({"message": "Role ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if self.role_service.role_exists(pk):
            self.role_service.delete_role(pk)
            return Response({"message": "Role deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
    def update(self, request:Request, pk=None):
        """
        Update a role by id.
        """
        if not pk:
            return Response({"message": "Role ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
            if self.role_service.role_exists(pk):
                role = self.role_service.get_role_by_id(pk)
                updated_role =self.role_service.update_role(pk, data)
                return Response({"role": updated_role}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
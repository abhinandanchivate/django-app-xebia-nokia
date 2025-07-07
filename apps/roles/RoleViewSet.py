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
	
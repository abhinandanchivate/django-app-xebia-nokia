
from rest_framework.viewsets import ViewSet
from injector import inject
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from apps.users.service import UserService
from apps.users.userserializer import UserSerializer
class UserViewSet(ViewSet):
    # inject the user_service
    @inject
    def __init__(self, user_service:UserService,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = user_service
    def create(self, request: Request):
        """
        Create a new user.
        List of business constraints:
        1. Username must be unique.
        2. Email must be unique and valid.
        3. Password must meet strong password criteria.
        4. First name and last name are optional.
        5. User must be active by default.
        """
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = self.user_service.create_user(data)
            return Response({"user": user}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def list(self, request: Request):
        """
        List all users.
        If no users are available, return a message indicating no data found.
        """
        users = self.user_service.get_all_users()
        if users:
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No data found"}, status=status.HTTP_404_NOT_FOUND)
    def retrieve(self, request: Request, pk=None):
        """
        Get a user by ID.
        """
        if not pk:
            return Response({"message": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self.user_service.get_user_by_id(pk)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    def destroy(self, request: Request, pk=None):
        """
        Delete a user by ID.
        """
        if not pk:
            return Response({"message": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        deleted = self.user_service.delete_user(pk)
        if deleted:
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    def update(self, request: Request, pk=None):
        """
        Update a user by ID.
        """
        if not pk:
            return Response({"message": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data
        serializer = UserSerializer(data=data, partial=True)  # Allow partial updates
        if serializer.is_valid():
            user = self.user_service.update_user(pk, data)
            if user:
                return Response({"user": user}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

     

    
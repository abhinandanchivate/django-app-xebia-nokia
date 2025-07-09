
from rest_framework.routers import DefaultRouter
from apps.roles.RoleViewSet import RoleViewSet
router  = DefaultRouter()
router.register(r'', RoleViewSet, basename='role')
# this roleviewset will hold complete CRUD operations for roles
# needs to be performed for a specific end points.

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register(r'roles', 'apps.roles.views.RoleViewSet', basename='roles')
# this roleviewset will hold complete CRUD operations for roles
# needs to be performed for a specific end points.

urlpatterns = router.urls
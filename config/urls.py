# points to the files that defines URL routes
from django.contrib import admin
from django.urls import path, include
from apps.roles import router as roles_router
from apps.users import router as users_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/roles/', include(roles_router.router.urls)),
    path('api/users/', include(users_router.router.urls)),
]
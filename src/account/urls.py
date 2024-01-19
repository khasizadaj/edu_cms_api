from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename="users")
router.register(r"groups", views.GroupViewSet, basename="groups")
router.register(r"permissions", views.PermissionViewSet, basename="permissions")

urlpatterns = [
    path(
        r"users-from-scratch",
        view=views.UsersListFromScratch.as_view(),
        name="users-from_scratch",
    ),
    path(
        r"users-from-model",
        view=views.UsersListFromModel.as_view(),
        name="users-from_model",
    ),
]

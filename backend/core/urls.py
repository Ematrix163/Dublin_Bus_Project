from django.urls import path, re_path
from .views import current_user, UserList
from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [
    re_path(r'^login/', obtain_jwt_token),
]
from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from module_user.views.UserViewSet import UserViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include
from api.views import CompaneyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompaneyViewSet)

urlpatterns = [
    path('', include(router.urls))
]

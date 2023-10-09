from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.urls import api_router

router = DefaultRouter()
router.registry.extend(api_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, ColorViewSet

app_name = 'model_view_set'

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'colors', ColorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

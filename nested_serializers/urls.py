from django.urls import path
from . import views

app_name = 'nested_serializers'

urlpatterns = [
    path('person/', views.PersonAPI.as_view(), name='person'),
]
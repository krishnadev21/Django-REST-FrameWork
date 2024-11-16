from django.urls import path
from . import views

app_name = 'api_view'

urlpatterns = [
    path('routes/', views.routes, name='routes'),
    path('person/', views.person, name='person'),   
]
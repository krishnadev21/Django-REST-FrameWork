from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('register/', views.Register.as_view() , name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('token-auth/', views.TokenAuthenticated.as_view(), name='token-auth'),
    path('paginator/', views.GetUserPaginator.as_view(), name='paginator')
]
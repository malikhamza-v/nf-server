from .views import CreateUserAPI, LoginAPI
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('register/', CreateUserAPI.as_view()),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout')
]
from django.urls import path
from knox import views as knox_views
from profile_api.views import (UserRegisterAPI,UserLoginAPI,UserDetailAPI,UserUpdateAPI)

urlpatterns = [
    path('register/', UserRegisterAPI.as_view()),
    path('login/', UserLoginAPI.as_view()),
    path('detail/', UserDetailAPI.as_view()),
    path('update/', UserUpdateAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),  
]
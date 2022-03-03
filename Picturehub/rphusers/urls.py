from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='authentication'),
    path('login/', views.loginpage, name= 'login'),
    path('logout/', views.logoutt, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profileform/<str:pk>/', views.profileform, name='profileform'),
]
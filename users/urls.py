from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as users_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', users_views.register, name='register-users'),
    path('profile/', users_views.profile, name='profile'),
]
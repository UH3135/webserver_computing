from django.urls import path
from .views import get_home_view, get_login_view, get_logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', get_login_view, name='login'),
    path('home/', get_home_view, name='home'),
    path('logout/', get_logout_view, name='logout')
]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.question_list, name='question-list'),
    path('questions/<int:pk>', views.question_detail, name="question-detail"),
    path('ask/', views.ask_question, name="ask-question"),
    path('login/', auth_views.LoginView.as_view(template_name='qa/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('attack/', views.csrf_attack, name='csrf-attack')
]
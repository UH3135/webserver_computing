from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('questions/', views.QuestionListAPIView.as_view(), name='question_list'),
    path('questions/new/', views.QuestionCreateAPIView.as_view(), name='question_update'),
    path('questions/<int:pk>/', views.QuestionDetailAPIView.as_view(), name='question_detail'),
    path('questions/<int:pk>/edit', views.QuestionUpdateAPIView.as_view(), name='question_create'),
    path('questions/<int:pk>/delete', views.QuestionDeleteAPIView.as_view(), name='question_delete'),
    # path('login/', auth_views.LoginView.as_view(template_name='qa/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='qa/logout.html'), name='logout')
]
from django.urls import path
from . import views


"""
urls.py is responsible for mapping the URLs in this 'account' app. 
"""

urlpatterns = [
    path('login/', views.login_view, name='login'), # URL line for login
    path('register/', views.register, name='register'),  # URL line for registration
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'), # URL line for student_dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'), # URL line for admin_dashboard
    path('logout/', views.logout_view, name='logout'),  # Logout URL
]

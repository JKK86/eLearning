from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.StudentsRegistrationView.as_view(), name='student_registration'),
]
"""eLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('course/list/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('course/add/', views.CourseCreateView.as_view(), name='course_create'),
    path('course/update/<int:pk>', views.CourseUpdateView.as_view(), name='course_update'),
    path('course/delete/<int:pk>', views.CourseDeleteView.as_view(), name='course_delete'),
    path('course/<int:pk>/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),

    path('course/module/<int:module_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('course/module/<int:module_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('course/content/<int:id>/delete/', views.ContentDeleteView.as_view(), 'module_content_delete'),
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(), 'module_content_list'),

]

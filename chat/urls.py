from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'chat'

urlpatterns = [
    path('room/<int:course_id>/', views.course_chat_room, name='course_chat_room'),
]

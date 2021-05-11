from django.shortcuts import render
from django.views.generic import ListView

from courses.models import Course


class ManageCourseListView(ListView):
    model = Course
    template_name = "courses/manage/course/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

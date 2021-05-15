from django.forms import inlineformset_factory

from courses.models import Course, Module

ModuleFormSet = inlineformset_factory(Course, Module,
                                      fields=['name', 'description'],
                                      extra=3,
                                      can_delete=True)

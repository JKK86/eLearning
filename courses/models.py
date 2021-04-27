from django.db import models

from eLearning import settings


class Subject(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa kategorii' )
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'kategoria'
        verbose_name_plural = 'Kategorie'


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nazwa kursu')
    slug = models.SlugField(max_length=255, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses', verbose_name='Kategorie')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses_created')
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name = 'kurs'
        verbose_name_plural = 'Kursy'


class Module(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nazwa modułu')
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'moduł'
        verbose_name_plural = 'Moduły'

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from eLearning import settings
from .fields import OrderField


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
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        return f'{self.order}. {self.name}'

    class Meta:
        verbose_name = 'moduł'
        verbose_name_plural = 'Moduły'
        ordering = ['order']


class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="contents")
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to={'model__in': ('text',
                                                                     'file',
                                                                     'image',
                                                                     'video')},
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        verbose_name = 'zawartość'
        verbose_name_plural = 'Zawartość'
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_related',
                              verbose_name='Użytkownik')
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    image = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()

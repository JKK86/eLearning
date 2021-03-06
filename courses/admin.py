from django.contrib import admin

from courses.models import Course, Module, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created']
    list_filter = ['subject', 'owner', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'overview']
    exclude = ['created', 'updated']
    inlines = [ModuleInline]


# Wykorzystanie witryny administracyjnej memcache
admin.site.index_template = 'memcache_status/admin_index.html'

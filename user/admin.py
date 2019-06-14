from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('title_id','title_name')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id','department_name')

from django.contrib import admin
from .models import Hiretuber
# Register your models here.
class HiretuberAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','tuber_name')

admin.site.register(Hiretuber,HiretuberAdmin);
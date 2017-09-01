from django.contrib import admin
from .models import Con

# Register your models here.
# admin.site.register(Con)
@admin.register(Con)
class ConAdmin(admin.ModelAdmin):
    list_display = ('content_list', 'flag', 'pubdate')
    list_filter = ('content_list',)
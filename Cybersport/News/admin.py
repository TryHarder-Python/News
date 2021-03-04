from django.contrib import admin
from .models import *

admin.site.register(Category)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_date', 'update_date', 'publish')
    list_filter = ('category', 'create_date', 'update_date', 'publish')
    search_fields = ('title', 'category', 'publish')
    list_display_links = ('title',)


admin.site.register(News, NewsAdmin)
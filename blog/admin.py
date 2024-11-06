from django.contrib import admin
from .models import BlogModel
# from import_export.admin import ImportExportModelAdmin

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'createdAt')

# for importing and exporting data
# class BlogAdmin(ImportExportModelAdmin):
#     list_display = ('title', 'createdAt')

admin.site.register(BlogModel, BlogAdmin)
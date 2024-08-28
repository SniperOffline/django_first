from django.contrib import admin
from blog.models import Category, Blog, Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class BlogAdmin(admin.ModelAdmin):
    search_fields = ('content','title')
    list_display = ('title', 'content')
    list_filter = ('title', 'author')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
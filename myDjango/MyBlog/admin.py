from django.contrib import admin

# Register your models here.
from MyBlog.models import BlogPost, Category, Tag, comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'pub')


class commentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'content', 'pub')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(comment, commentAdmin)

from django.contrib import admin

# Register your models here.
from myBlog.models import Catagory, Tag, Blog, Comment


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'catagory', 'content', 'pub',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'content', 'pub')


admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)

from django.db import models


# Create your models here.

# 博客分类
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField('名称', max_length=100)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField('名称', max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField('标题', max_length=100)
    author = models.CharField('作者', max_length=10)
    content = models.TextField(help_text='博客内容')
    pub = models.DateTimeField('发布时间', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='类别',on_delete=CASCADE)  # 多对一
    tag = models.ManyToManyField(Tag, verbose_name='标签')  # 多对多

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class comment(models.Model):
    blog = models.ForeignKey(BlogPost, verbose_name='博客',on_delete=CASCADE)
    name = models.CharField('称呼', max_length=10)
    email = models.CharField('邮箱', max_length=20)
    content = models.CharField('内容', max_length=240)
    pub = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

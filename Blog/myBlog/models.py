from django.db import models


# Create your models here.
class Catagory(models.Model):
    name = models.CharField('名称', max_length=20)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('名称', max_length=20)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)  # 多对一
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    title = models.CharField('标题', max_length=30)
    author = models.CharField('作者', max_length=20)
    content = models.TextField('内容')
    pub = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField('称呼', max_length=20)
    email = models.EmailField('邮箱')
    content = models.TextField('内容')
    pub = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class User(models.Model):
    username = models.CharField('名字', max_length=20)
    password = models.CharField('密码', max_length=20)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

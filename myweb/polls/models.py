import datetime


from django.db import models

# Create your models here.
# 问题模型
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish date')

    # 返回字符串
    def __str__(self):
        return self.question_text

    # 是否超时
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# 选择模型
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)  # 票数默认为零

    def __str__(self):
        return self.choice_text

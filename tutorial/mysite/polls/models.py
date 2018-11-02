import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # 質問内容(Char型)
    question_text = models.CharField(max_length=200)
    # 投稿日時(DateTime型)
    pub_date = models.DateTimeField('data published')

    # 見やすくする
    def __str__(self):
        return self.question_text

    # 1日以内の投稿であるかどうか
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    # 紐付けするQuestionを格納
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # Int型
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

from datetime import datetime

from django.db import models

class Thread(models.Model):
    title = models.CharField('Title', max_length=200, blank=False)
    message = models.TextField('Message', blank=False)
    pub_date = models.DateTimeField('Published date', auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'thread'

    def __str__(self):
        return self.message

class Comment(models.Model):
    thread = models.ForeignKey(Thread, verbose_name='thread', on_delete=models.CASCADE)
    message = models.CharField('Message', max_length=200, blank=False)
    pub_date = models.DateTimeField('Published date', auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'comment'

    def __str__(self):
        return self.message

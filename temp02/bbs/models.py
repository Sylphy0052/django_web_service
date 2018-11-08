from django.db import models
from django.contrib.auth.models import User

# 掲示板
class Bbs(models.Model):
    # 名前
    name = models.CharField(max_length=30, unique=True)
    # 説明
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# スレッド
class Thread(models.Model):
    # スレッド名
    name = models.CharField(max_length=255)
    # 最終更新日時
    last_updated = models.DateTimeField(auto_now_add=True)
    # Bbs
    bbs = models.ForeignKey(Bbs, related_name='thread', on_delete=models.CASCADE)
    # スレを建てた人
    starter = models.ForeignKey(User, related_name='thread', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    # 本文
    message = models.TextField(max_length=1024)
    # スレッド名
    thread = models.ForeignKey(Thread, related_name='post', on_delete=models.CASCADE)
    # 書き込んだ時間
    created_at = models.DateTimeField(auto_now_add=True)
    # アップデートした時間
    updated_at = models.DateTimeField(null=True)
    # 誰が書き込んだか
    created_by = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    # 誰がアップデートしたか
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

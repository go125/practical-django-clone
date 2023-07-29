from django.conf import settings
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField("タグ名", max_length=32)
    created_at = models.DateTimeField('日付', auto_now_add=True)

    def __str__(self):
        return self.name

class Snippet(models.Model):
    title=models.CharField('タイトル',max_length=128)
    tag = models.ManyToManyField(
    Tag, verbose_name='タグ')
    code=models.TextField('コード',blank=True)
    description=models.TextField('説明',blank=True)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)
    created_at=models.DateTimeField("投稿日", auto_now_add=True)
    updated_at=models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title

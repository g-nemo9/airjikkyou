from django.db import models


# Create your models here.
class Post(models.Model):
    """投稿内容のモデル"""
    class Meta:
        db_table = 'post'

    title = models.CharField(verbose_name='タイトル', max_length=140)
    start_time = models.DateTimeField(verbose_name='開始時刻')
    episode = models.IntegerField(verbose_name='話数', null=True)
    comment = models.CharField(verbose_name='コメント', max_length=140)

    def __str__(self):
        return self.title


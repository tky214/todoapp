from django.db import models
from django.contrib.auth.models import User #djangoにあるUserを使う
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)#CASCADE=userが消された場合タスクを消す、
    title = models.CharField(max_length=100)#１００文字まで
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)#作ったタイムスタンプを自動的に追加

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["completed"]#順番を並び替えるデータの指定
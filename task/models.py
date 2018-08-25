from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务列表'


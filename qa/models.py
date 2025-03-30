from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    like = models.IntegerField()
    unlike = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(null=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(null=True)


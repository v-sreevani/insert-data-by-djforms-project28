from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name


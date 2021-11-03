from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='姓名')
    age = models.IntegerField(verbose_name="年龄")
    score = models.IntegerField(verbose_name="成绩")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name

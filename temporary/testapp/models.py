
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=200)
    contact=models.CharField(max_length=19)

    def __str__(self):
        return self.name


class St_user(models.Model):
    name=models.CharField(max_length=20)
    pawrd=models.CharField(max_length=255, blank=False, null=False)
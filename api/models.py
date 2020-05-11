from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    fullName = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=False)
    sex = models.CharField(max_length=10)
    matric_no = models.CharField(max_length=20)
    image = models.FileField(upload_to='media', null=False, blank=False, default='')
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.user

from django.db import models


class Student(models.Model):
    group = models.CharField(max_length=50, blank=True, null=True)
    fio = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    financing_form = models.CharField(max_length=50, blank=True, null=True)
    profcard = models.CharField(max_length=50, blank=True, null=True)
    student_book = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    telegram_id = models.CharField(max_length=50, blank=True, null=True)

from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    about = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    duration_months = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    teacher = models.ManyToManyField(to=Teacher)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})

    def list_teachers(self):
        return ', '.join(str(teacher) for teacher in self.teacher.all())


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(to=Course)

    def __str__(self):
        return f"{self.name} {self.surname}"

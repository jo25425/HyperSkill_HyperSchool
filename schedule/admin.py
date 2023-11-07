from django.contrib import admin

from schedule.models import Course, Teacher, Student


admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)

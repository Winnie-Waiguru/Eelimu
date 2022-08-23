from multiprocessing.connection import Client
from django.contrib import admin

from home.models import Course, Fees, Payment, Schedule, Student, Trainer, Visitor

# Register your models here.
admin.site.register(Visitor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(Trainer)
admin.site.register(Fees)
admin.site.register(Payment)
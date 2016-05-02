import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


"""
Generates course choices from file:

file = open('/Users/fishb1jw/capstone_project/note_exchange/notes_app/courses.txt')
COURSE_CHOICES = tuple((choice,choice) for choice in file.readline().splitlines())

"""


class Course(models.Model):

    subject = models.CharField(max_length = 255)

    def __unicode__(self):

      return self.subject

class Document(models.Model):


    file = models.FileField(upload_to='documents/%Y/%m/%d')
    subject_number = models.PositiveIntegerField(default=False)
    subject_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course)
    description = models.TextField(default=None)
    pub_date = models.DateField(default=timezone.now())

    def __unicode__(self):

      return self.title

    def get_absolute_url(self):

      return "/main/get/%i/" % self.id

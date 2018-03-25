from __future__ import unicode_literals

from django.db import models
# from django.core.validators import MinLengthValidator
# use it by calling MinLengthValidator(#)

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['full_name']) < 5:
            errors["full_name"] = "Course name should be >5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Course description should be >15 characters"
        return errors

class Course(models.Model):
    full_name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # Replace the old Manager with our own Manager
    objects = CourseManager()


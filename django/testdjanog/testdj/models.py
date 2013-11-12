from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30, default='d')
    update_on = models.DateTimeField(auto_now=True)
    #def save(self, *args, **kwargs):
    #       self.update_on = timezone.now()
    #       return self.super(Person, self).save(*args, **kwargs)
class User(models.Model):
    name = models.CharField(max_length=30, default='dd')
    createTime = models.DateTimeField(auto_now_add=True)

class Te(models.Model):
    update_on = models.DateTimeField(auto_now_add=True, auto_now=True)

print "fe-------"

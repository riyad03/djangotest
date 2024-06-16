from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

# Create your models here.


class MyUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You may want to hash this
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title



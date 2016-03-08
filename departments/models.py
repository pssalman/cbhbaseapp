from django.db import models
from authentication.models import Account


# Create your models here.

class Department(models.Model):
    author = models.ForeignKey(Account)
    department_name = models.CharField(max_length=40, unique=True)
    department_code = models.CharField(max_length=3, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.department_name)

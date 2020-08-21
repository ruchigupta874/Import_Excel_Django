from django.db import models
from django.urls import reverse
# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()

    def __str__(self):
        return self.name;

    def get_absolute_url(self):
        return reverse("emp_list")


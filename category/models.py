from django.db import models
from task.models import TaskModel

# Create your models here.
class CategoryModel(models.Model):
    CategoryName = models.CharField(max_length = 100)
    task = models.ManyToManyField(TaskModel)



    def __str__(self):
        return self.CategoryName
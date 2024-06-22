from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)

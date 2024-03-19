from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    page_number = models.IntegerField()
    publish_data = models.DateField()
    stock = models.IntegerField()
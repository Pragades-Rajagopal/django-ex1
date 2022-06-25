from django.db import models
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
imagePath = os.path.join(BASE_DIR, 'tmp')

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state_province = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return self.name
    # explicitly returning output with order_by "name"
    class Meta:
        ordering = ["name"]


class Author(models.Model):
    salutation = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    headshot = models.ImageField(upload_to=imagePath)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title



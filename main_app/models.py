from django.db import models
import datetime


class Image(models.Model):
    """the main image database entry. stores all the necessary information
    about an image file that has been submitted."""
    username = models.CharField(max_length=80, default='')
    name = models.CharField(max_length=80, default='')
    description = models.CharField(max_length=300, default='')
    image_file = models.FileField(default='')
    date_created = models.DateTimeField(default=datetime.datetime.now())
    date_modified = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.name} uploaded by {self.username}'

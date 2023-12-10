from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

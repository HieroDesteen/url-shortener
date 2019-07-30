from django.db import models

# Create your models here.
class Url_match(models.Model):
    long_url = models.TextField()
    short_url=models.TextField()
    def __str__(self):
        return self.long_url
from django.db import models

# Create your models here.
class Url_match(models.Model):
    long_url = models.TextField()
    short_url=models.TextField(unique=True)
    call_counter=models.IntegerField(default=0)
    def __str__(self):
        return self.long_url
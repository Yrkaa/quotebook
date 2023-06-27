from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.TextField(blank=False)
    author = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return str(self.id)
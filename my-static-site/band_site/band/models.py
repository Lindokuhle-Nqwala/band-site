from django.db import models

# Create your models here.
class Concert(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
         return f"{self.title} @ {self.venue} on {self.date}"

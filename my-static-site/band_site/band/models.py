from django.db import models

class Concert(models.Model):
    """
    Model representing a concert event.

    Attributes:
        name (str): Name of the concert.
        date (datetime): Date and time of the concert.
        venue (str): Venue where the concert will be held.
        description (str): Description of the concert.
    """
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """
        Returns a readable string representation of the concert.
        """
        return f"{self.name} @ {self.venue} on {self.date}"

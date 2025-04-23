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


class BandMember(models.Model):
    """
    Represents a member of the band with a name and instrument.
    """
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)


    def __str__(self):
        """
        Returns a readable string representation of the concert.
        """
        return f"{self.name} @ {self.venue} on {self.date}"


class BandMember(models.Model):
    """
    Represents a member of the band with a name and instrument.
    """
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.instrument})"


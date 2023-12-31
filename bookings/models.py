from django.db import models
from django.contrib.auth.models import User


# Choice fields
LEVEL = (
    ("beginner", "Beginner"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced")
)

TIME = (
    (1, "09:00-11:00"),
    (2, "12:00-14:00"),
    (3, "15:00-17:00"),
    (4, "18:00-20:00")
)


class Booking(models.Model):
    """
    Model to allow user to make a booking
    """
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client")
    level = models.CharField(max_length=15, choices=LEVEL, default="beginner")
    day = models.DateField()
    time = models.IntegerField(choices=TIME, default=1)

    class Meta:
        ordering = ['day']

    def __str__(self):
        return str(self.level)

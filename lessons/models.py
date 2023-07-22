from django.db import models
from django.contrib.auth.models import User

# Choice fields
LEVEL = (
    ("beginner", "Beginner"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced")
)

DAY = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
)


class Lessons(models.Model):
    """
    A model to create the tennis lesson timetables
    """
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=15, choices=LEVEL, default="beginner")
    date = models.IntegerField(choices=DAY, default=1)
    morning = models.BooleanField(default=False)
    early_afternoon = models.BooleanField(default=False)
    late_afternoon = models.BooleanField(default=False)
    evening = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.level)

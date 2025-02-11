from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    time = models.TimeField()
    refill_reminder = models.IntegerField(help_text="Days before refill reminder", default=3)

    def __str__(self):
        return f"{self.name} - {self.dosage}"

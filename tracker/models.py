from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    time = models.TimeField()
    fcm_token = models.TextField(blank=True, null=True)  # Store FCM token for notifications

    def __str__(self):
        return f"{self.name} - {self.dosage}"

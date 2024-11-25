from django.db import models
from django.conf import settings

class Izin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.start_date} to {self.end_date}"

from django.db import models
from django.conf import settings

class Yoklama(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    late_minutes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

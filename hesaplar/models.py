from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    # Ek alanlar
    is_authorized_personnel = models.BooleanField(default=False, verbose_name='Yetkili Personel mi?')
    annual_leave = models.DecimalField(max_digits=5, decimal_places=2, default=15.00, verbose_name='Yıllık İzin (Gün)')

    def __str__(self):
        return self.username

    # save metodunu override ediyoruz
    def save(self, *args, **kwargs):
        if self.annual_leave < 3:
            # Yetkili personele bildirim gönderme
            self.send_low_leave_notification()
        super().save(*args, **kwargs)

    # Bildirim gönderme fonksiyonu
    def send_low_leave_notification(self):
        User = get_user_model()
        authorized_personnel = User.objects.filter(is_authorized_personnel=True)
        subject = 'Yıllık İzin Uyarısı'
        message = f'{self.get_full_name()} adlı personelin yıllık izni 3 günden az kaldı.'
        from_email = 'noreply@sirket.com'
        recipient_list = [person.email for person in authorized_personnel if person.email]
        send_mail(subject, message, from_email, recipient_list)

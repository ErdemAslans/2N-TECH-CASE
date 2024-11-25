from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from yoklama.models import Yoklama
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_authorized_personnel:
                return redirect('yetkili_dashboard')
            else:
                return redirect('personel_dashboard')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')
    return render(request, 'hesaplar/login.html')

def send_late_notification(user, late_minutes):
    # Yetkili kullanıcıları al
    User = get_user_model()
    authorized_personnel = User.objects.filter(is_authorized_personnel=True)
    subject = 'Personel Geç Kalma Bildirimi'
    message = f'{user.get_full_name()} adlı personel {late_minutes} dakika geç kaldı.'
    from_email = 'noreply@sirket.com'
    recipient_list = [person.email for person in authorized_personnel]
    send_mail(subject, message, from_email, recipient_list)


def user_logout(request):
    # Çıkış zamanını kaydetme
    if request.user.is_authenticated:
        today = timezone.now().date()
        try:
            yoklama = Yoklama.objects.get(user=request.user, date=today)
            yoklama.check_out = timezone.now().time()
            yoklama.save()
        except Yoklama.DoesNotExist:
            pass
    logout(request)
    return redirect('hesaplar:login')

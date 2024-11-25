from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from yoklama.models import Yoklama

@login_required
def dashboard(request):
    today = timezone.now().date()
    yoklama, created = Yoklama.objects.get_or_create(user=request.user, date=today)
    if created or yoklama.check_in is None:
        yoklama.check_in = timezone.now().time()
        # Geç kalma hesaplaması
        calisma_baslangic_saati = timezone.datetime.combine(today, timezone.datetime.strptime('08:00', '%H:%M').time())
        gecikme = timezone.now() - calisma_baslangic_saati
        if gecikme.total_seconds() > 0:
            yoklama.late_minutes = int(gecikme.total_seconds() // 60)
            # Yıllık izinden düşme işlemi
            izin_eksiltme = yoklama.late_minutes / (60 * 8)  # 8 saatlik çalışma günü varsayımı
            request.user.annual_leave -= izin_eksiltme
            request.user.save()
            # Yetkiliye bildirim gönderme (daha sonra eklenecek)
        yoklama.save()
    return render(request, 'personel/dashboard.html', {'yoklama': yoklama})

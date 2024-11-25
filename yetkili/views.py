from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Kullanıcıya mesaj göstermek için
from izinler.models import Izin  # Izin modelini doğru şekilde import ediyoruz
from django.utils import timezone
from django.db.models import Sum
from yoklama.models import Yoklama
from hesaplar.models import CustomUser
@login_required
def izin_talepleri(request):
    izinler = Izin.objects.filter(is_approved=False, is_rejected=False)
    return render(request, 'yetkili/izin_talepleri.html', {'izinler': izinler})

@login_required
def izin_onayla(request, izin_id):
    izin = get_object_or_404(Izin, id=izin_id)  # Hata durumunda 404 döner
    izin.is_approved = True
    izin.save()
    # Personelin yıllık izninden düşme işlemi
    izin_suresi = (izin.end_date - izin.start_date).days + 1
    izin.user.annual_leave -= izin_suresi
    izin.user.save()
    messages.success(request, 'İzin talebi onaylandı.')
    return redirect('yetkili:izin_talepleri')

@login_required
def izin_reddet(request, izin_id):
    izin = get_object_or_404(Izin, id=izin_id)  # Hata durumunda 404 döner
    izin.is_rejected = True
    izin.save()
    messages.success(request, 'İzin talebi reddedildi.')
    return redirect('yetkili:izin_talepleri')

@login_required
def aylik_rapor(request):
    today = timezone.now()
    current_month = today.month
    personeller = CustomUser.objects.filter(is_authorized_personnel=False)
    rapor = []
    for personel in personeller:
        toplam_calisma_suresi = Yoklama.objects.filter(
            user=personel,
            date__month=current_month
        ).aggregate(toplam_sure=Sum('late_minutes'))
        rapor.append({
            'personel': personel,
            'toplam_calisma_suresi': toplam_calisma_suresi['toplam_sure'] or 0
        })
    return render(request, 'yetkili/aylik_rapor.html', {'rapor': rapor})
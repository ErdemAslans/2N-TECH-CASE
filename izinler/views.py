from django.shortcuts import render, redirect
from .forms import IzinForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def izin_talep_et(request):
    if request.method == 'POST':
        form = IzinForm(request.POST)
        if form.is_valid():
            izin = form.save(commit=False)
            izin.user = request.user
            izin.save()
            messages.success(request, 'İzin talebiniz alınmıştır.')
            return redirect('personel:dashboard')
    else:
        form = IzinForm()
    return render(request, 'personel/izin_talep.html', {'form': form})

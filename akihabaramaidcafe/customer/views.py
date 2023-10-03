from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Menu
from .decorators import kode_otentikasi, validasi_user
from servercafe.models import Masuk

def othen(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id:
            try:
                user = Masuk.objects.get(id=id)
                if user:
                    request.session['user_id'] = user.id
                    messages.success(request, 'Login berhasil.')
                    return redirect('index')  # Ganti 'home' dengan nama URL halaman setelah login
                else:
                    messages.error(request, 'Login gagal. ID tidak valid.')
            except Masuk.DoesNotExist:
                messages.error(request, 'Login gagal. ID tidak valid.')
        else:
            messages.error(request, 'Login gagal. ID tidak valid.')
    return render(request, 'othentikasi.html')

@kode_otentikasi
@validasi_user
def index(request):
    makanan = Menu.objects.filter(kategori="makanan")
    minuman = Menu.objects.filter(kategori="minuman")
    sidedish = Menu.objects.filter(kategori="side dish")
    item = { "makanan": makanan,
            "minuman": minuman,
            "sidedish": sidedish,
    }
    return render(request, "customer.html", item)
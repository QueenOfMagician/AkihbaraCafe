from functools import wraps
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from servercafe.models import Masuk

def kode_otentikasi(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_id = request.session.get('user_id', None)
        if user_id is not None:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("masuk")
    return _wrapped_view

def validasi_user(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user_id = request.session.get('user_id', None)
        if user_id is not None:
            try:
                user = Masuk.objects.get(id=user_id)
                if user:
                    return view_func(request, *args, **kwargs)
            except Masuk.DoesNotExist:
                messages.error(request, "Maaf Untuk Sesi Telah Berkhir")  
            messages.error(request, 'Login gagal. ID tidak valid atau sudah dihapus.')
        return redirect('masuk')
    return _wrapped_view
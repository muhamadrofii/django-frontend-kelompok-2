from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
# from allauth.account.auth_backends import AuthenticationBackend


def custom_login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Autentikasi dengan menggunakan email dan password
        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect("account_dashboard")
        else:
            messages.error(request, "Invalid email or password")
    
    return render(request, "account/loginForm.html")


def custom_register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Validasi password dan konfirmasi password
        # if password != confirm_password:
        #     messages.error(request, "Password dan konfirmasi password tidak cocok.")
        #     return render(request, "account/registerForm.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "username sudah terdaftar.")
            return render(request, "account/registerForm.html")

        # Cek apakah email sudah terdaftar
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email sudah terdaftar.")
            return render(request, "account/registerForm.html")

        # Membuat user baru
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Login otomatis setelah registrasi
            # login(request, user)

            # Memberikan pesan sukses dan redirect ke halaman setelah login
            messages.success(request, "Akun Anda berhasil dibuat. Anda sekarang login.")
            return redirect("index")  # Ganti dengan nama URL yang sesuai untuk halaman setelah login

        except ValidationError:
            messages.error(request, "Terjadi kesalahan. Coba lagi.")
    
    return render(request, "account/registerForm.html")

@login_required
def account_dashboard(request):
    print("User:", request.user)  # Debug: Prints logged-in user
    return render(request, 'account/beranda.html')

def auto_logout_view(request):
    logout(request)  # Logs the user out
    return redirect('/')  # Redirects to the index page (or any other page)

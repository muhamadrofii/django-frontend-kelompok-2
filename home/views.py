from django.shortcuts import render
from .forms import ContactUsForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def index(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Save the form data to the ContactUs model
            form.save()
            # Optionally, display a success message
            return render(request, 'index.html', {'form': form, 'message': 'Terima kasih atas pesan Anda!'})
    else:
        form = ContactUsForm()

    return render(request, 'index.html', {'form': form})

def news(request):
    return render(request, 'news.html')

def aboutus(request):
    return render(request, 'aboutUs.html')
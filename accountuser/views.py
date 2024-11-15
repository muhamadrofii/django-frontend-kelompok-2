from django.shortcuts import render

# Create your views here.


def learning(request):
    return render(request, 'account/videoLearning.html')
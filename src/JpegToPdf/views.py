from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html',{})

def upload_JpegToPdf(request):
    return render

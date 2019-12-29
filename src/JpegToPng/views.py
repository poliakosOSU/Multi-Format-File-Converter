from django.shortcuts import render, redirect

from converters.ToPng_converter import ConvertFile
from .forms import JpegToPngForm
from .models import Jpeg, Png

# upload Jpeg to database and dispaly current data from database
def upload_JpegToPng(request):
    if request.method == 'POST':
        form = JpegToPngForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Jpeg(image_file=request.FILES['image_file'], file_name=request.FILES['image_file'].name)
            instance.save()
            print("FORM SAVED")
        the_uploaded_files = Jpeg.objects.all()
        form = JpegToPngForm()
        return render(request, 'JpegToPng/upload.html',{
            'the_uploaded_files': the_uploaded_files,
            'form': form
        })
    else:
        the_uploaded_files = Jpeg.objects.all()
        form = JpegToPngForm()
        return render(request, 'JpegToPng/upload.html', {
            'the_uploaded_files': the_uploaded_files,
            'form': form
            })

# delete Jpeg From database (method used for testing)
def delete_JpegToPng(request, pk):
    if request.method == 'POST':
        file = Jpeg.objects.get(pk=pk)
        file.delete()
    return redirect('upload_JpegToPng')

def convert_JpegToPng(request, pk):
    if request.method == 'POST':
        file = Jpeg.objects.get(pk=pk)
        image_name, image_url = ConvertFile(file.image_file.url)
        print("COVER")
        print(file.image_file.url)
        instance = Png(file_name = image_name, image_file=image_url, cover=file.image_file)
        instance.save()
        # later add delete sequence for Jpeg
    return redirect('upload_JpegToPng')

def display_pngs_JpegToPng(request):
    pngs = Png.objects.all()
    return render(request, 'JpegToPng/download.html', {
        'pngs': pngs
    })

def delete_converted_JpegToPng(request, pk):
    if request.method == 'POST':
        file = Png.objects.get(pk=pk)
        file.delete()
    return redirect('display_pngs_JpegToPng')

from django.shortcuts import render, redirect

from converters.ToJpeg_converter import ConvertFile
from .forms import PngToJpegForm
from .models import Jpeg, Png

def upload_PngToJpeg(request):
    if request.method == 'POST':
        form = PngToJpegForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Png(image_file=request.FILES['image_file'], file_name=request.FILES['image_file'].name)
            instance.save()
            print("FORM SAVED")
        the_uploaded_files = Png.objects.all()
        form = PngToJpegForm()
        return render(request, 'PngToJpeg/upload.html',{
            'the_uploaded_files': the_uploaded_files,
            'form': form
        })
    else:
        the_uploaded_files = Png.objects.all()
        form = PngToJpegForm()
        return render(request, 'PngToJpeg/upload.html', {
            'the_uploaded_files': the_uploaded_files,
            'form': form
            })

# delete Png From database (method used for testing)
def delete_PngToJpeg(request, pk):
    if request.method == 'POST':
        file = Png.objects.get(pk=pk)
        file.delete()
    return redirect('upload_PngToJpeg')

def convert_PngToJpeg(request, pk):
    if request.method == 'POST':
        file = Png.objects.get(pk=pk)
        image_name, image_url = ConvertFile(file.image_file.url)
        print("COVER")
        print(file.image_file.url)
        instance = Jpeg(file_name = image_name, image_file=image_url, cover=file.image_file)
        instance.save()
        # later add delete sequence for Png
    return redirect('upload_PngToJpeg')

def display_jpegs_PngToJpeg(request):
    jpegs = Jpeg.objects.all()
    return render(request, 'PngToJpeg/download.html',{
        'jpegs': jpegs
    })

def delete_converted_PngToJpeg(request, pk):
    if request.method == 'POST':
        file = Jpeg.objects.get(pk=pk)
        file.delete()
    return redirect('display_jpegs_PngToJpeg')

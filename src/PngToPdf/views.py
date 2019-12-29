from django.shortcuts import render, redirect


from converters.ToPdf_converter import ConvertFile
from .forms import PngToPdfForm
from .models import Png, Pdf

def upload_PngToPdf(request):
    if request.method == 'POST':
        form = PngToPdfForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Png(image_file=request.FILES['image_file'], file_name=request.FILES['image_file'].name)
            instance.save()
        the_uploaded_files = Png.objects.all()
        form = PngToPdfForm()
        return render(request, 'PngToPdf/upload.html', {
            'the_uploaded_files': the_uploaded_files,
            'form': form
        })
    else:
        the_uploaded_files = Png.objects.all()
        form = PngToPdfForm()
        return render(request, 'PngToPdf/upload.html', {
            'the_uploaded_files': the_uploaded_files,
            'form': form
        })

def delete_PngToPdf(request, pk):
    if request.method == 'POST':
        file = Png.objects.get(pk=pk)
        file.delete()
    return redirect('upload_PngToPdf')

def convert_PngToPdf(request, pk):
    if request.method == 'POST':
        file = Png.objects.get(pk=pk)
        pdf_name, pdf_url = ConvertFile(file.image_file.url)
        print("COVER")
        print(file.image_file.url)
        instance = Pdf(file_name = pdf_name, pdf_file=pdf_url, cover=file.image_file)
        instance.save()
        # later add delete sequence for Png

    return redirect('upload_PngToPdf')

def display_pdfs_PngToPdf(request):
    pdfs = Pdf.objects.all()
    return render(request, 'PngToPdf/download.html', {
        'pdfs': pdfs
    })

def delete_converted_PngToPdf(request, pk):
    if request.method == 'POST':
        file = Pdf.objects.get(pk=pk)
        file.delete()
    return redirect('display_pdfs_PngToPdf')

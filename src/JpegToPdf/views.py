from django.shortcuts import render, redirect

from converters.ToPdf_converter import ConvertFile
from .forms import JpegToPdfForm
from .models import Jpeg, Pdf

# displays home page which contains links to different convertersion fromats
def home_view(request, *args, **kwargs):
    return render(request, 'home.html',{})


# upload Jpeg to database and dispaly current data from database
def upload_JpegToPdf(request):
    if request.method == 'POST':
        form = JpegToPdfForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Jpeg(image_file=request.FILES['image_file'], file_name=request.FILES['image_file'].name)
            instance.save()
            print("FORM SAVED")
        the_uploaded_files = Jpeg.objects.all()
        form = JpegToPdfForm()
        return render(request, 'JpegToPdf/upload.html',{
            'the_uploaded_files': the_uploaded_files,
            'form': form
        })
    else:
        the_uploaded_files = Jpeg.objects.all()
        form = JpegToPdfForm()
        return render(request, 'JpegToPdf/upload.html', {
            'the_uploaded_files': the_uploaded_files,
            'form': form
            })

# delete Jpeg From database (method used for testing)
def delete_JpegToPdf(request, pk):
    if request.method == 'POST':
        file = Jpeg.objects.get(pk=pk)
        file.delete()
    return redirect('upload_JpegToPdf')


def convert_JpegToPdf(request, pk):
    if request.method == 'POST':
        file = Jpeg.objects.get(pk=pk)
        pdf_name, pdf_url = ConvertFile(file.image_file.url)
        print("COVER")
        print(file.image_file.url)
        instance = Pdf(file_name = pdf_name, pdf_file=pdf_url, cover=file.image_file)
        instance.save()
        # later add delete sequence for Jpeg
    return redirect('upload_JpegToPdf')

def display_pdfs_JpegToPdf(request):
    pdfs = Pdf.objects.all()
    return render(request, 'JpegToPdf/download.html', {
        'pdfs': pdfs
    })

def delete_converted_JpegToPdf(request, pk):
    if request.method == 'POST':
        file = Pdf.objects.get(pk=pk)
        file.delete()
    return redirect('display_pdfs_JpegToPdf')

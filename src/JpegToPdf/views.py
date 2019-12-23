from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html',{})

def upload_JpegToPdf(request):
    if request.method == 'POST':
        form = JpegToPdfForm.save(commit=False)
        form.file_name = request.Files['file'.name]
        form.save()
        # form = JpegToPdfForm(request.POST, request.FIlES)
        # if form.is_valid():
        #     form.save()
        #
        # file = Jpeg.objects.get
    form = JpegToPdfForm()
    uploaded_files = Jpeg.objects.all()
    return render(request, 'upload.html', {
        'uploaded_files': uploaded_files,
        'form': form
    })

# def delete_JpegToPdf:

# def delete_converted_JpegToPdf:

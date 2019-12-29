from django.db import models

class Png(models.Model):
    file_name  = models.CharField(max_length=100, null=True, blank=True)
    image_file = models.FileField(upload_to='PngToPdf/original/',null=True)

class Pdf(models.Model):
    file_name = models.CharField(max_length=100)
    pdf_file  = models.FileField(upload_to='PngToPdf/converted/')
    cover     = models.FileField(upload_to='PngToPdf/original/', null=True, blank=True)

    def __str__(self):
        return self.file_name

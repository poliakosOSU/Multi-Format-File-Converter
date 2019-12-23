from django.db import models

# Create your models here.
class Jpeg(models.Model):
    file_name  = models.CharField(max_length=100, null=True, blank=True)
    file  = models.FileField(upload_to='JpegToPdf/original/')
    # cover = models.ImageField(upload_to='JpegToPdf/original/', null=True, blank=True)

class Pdf(models.Model):
    file_name  = models.CharField(max_length=100)
    file  = models.FileField(upload_to='JpegToPdf/converted/')
    cover = models.ImageField(upload_to='JpegToPdf/original/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        # self.cover.delete()
        super().delete(*args, **kwargs) #Calls the "real" save() method

    def Pdf(self, *args, **kwargs):
        self.name.delete()
        # self.file.delete()
        super().Pdf(*args, **kwargs)

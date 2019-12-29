from django.db import models

class Jpeg(models.Model):
    file_name  = models.CharField(max_length=100, null=True, blank=True)
    image_file = models.FileField(upload_to='JpegToPdf/original/',null=True)
    # cover = models.ImageField(upload_to='JpegToPdf/original/', null=True, blank=True)

class Pdf(models.Model):
    file_name = models.CharField(max_length=100)
    pdf_file  = models.FileField(upload_to='JpegToPdf/converted/')
    cover     = models.FileField(upload_to='JpegToPdf/original/', null=True, blank=True)

    def __str__(self):
        return self.file_name

    # def delete(self, *args, **kwargs):
    #     self.image_file.delete()
    #     # self.cover.delete()
    #     super().delete(*args, **kwargs) #Calls the "real" save() method

    # def Pdf_delete(self, *args, **kwargs):
    #     self.name.delete()
    #     # self.file.delete()
    #     super().Pdf(*args, **kwargs)

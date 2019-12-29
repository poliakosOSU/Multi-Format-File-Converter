from django.db import models

class Jpeg(models.Model):
    file_name  = models.CharField(max_length=100, null=True, blank=True)
    image_file = models.FileField(upload_to='JpegToPng/original/',null=True)

class Png(models.Model):
    file_name  = models.CharField(max_length=100, null=True, blank=True)
    image_file = models.FileField(upload_to='JpegToPng/converted/', null=True)
    cover      = models.FileField(upload_to='JpegToPng/original/', null=True, blank=True)

    def __str__(self):
        return self.file_name

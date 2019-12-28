"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from JpegToPdf.views import (
    home_view,
    # Jpeg_display,
    upload_JpegToPdf,
    delete_JpegToPdf,
    convert_JpegToPdf,
    display_pdfs_JpegToPdf,
    delete_converted_JpegToPdf,

)

urlpatterns = [
    path('', home_view, name='home_view'),
    # path('JpegToPdf/upload/dispaly', Jpeg_display, name='Jpeg_display'),
    path('JpegToPdf/upload', upload_JpegToPdf, name='upload_JpegToPdf'),
    path('JpegTopdf/upload/<int:pk>', delete_JpegToPdf, name='delete_JpegToPdf'),
    path('JpegTopdf/upload/<int:pk>/convert', convert_JpegToPdf, name='convert_JpegToPdf'),
    path('JpegToPdf/download', display_pdfs_JpegToPdf, name='display_pdfs_JpegToPdf'),
    path('JpegTopdf/download/<int:pk>', delete_converted_JpegToPdf, name='delete_converted_JpegToPdf'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

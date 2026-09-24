"""
URL configuration for resume_folder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from resume_maker.views import *#here we imported all views functions
urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal/', personal, name="personal"),
    path('skill/', skill, name="skill"),
    path('education/',edu , name="edu"), # here edu is view's function name not name=edu.
    path('experience/',exp , name="exp"),
    path('other/', other, name="other"),
    path('education2/', edu2, name="edu2"),
    path('resumemaker/', resumemaker, name="resumemaker"),
    path('graduation/', ug_pg, name="ug_pg"),
    path('undergraduate/', ug, name="ug_page"),
    path('graduated/', pg, name="pg_page"),
    path('experienceyesorno/', expornot, name="expornot"),
    path('noexperience/', yes_exp, name="yes"),
    path('yesexperience/', no_exp, name="no"),


]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
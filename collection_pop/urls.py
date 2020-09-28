"""collection_pop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("users/", include("django.contrib.auth.urls")),
    path("figurines/", include("figurines.urls", namespace="figurines")),
    path("legal_notice/", views.legal_notice, name="legal_notice"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("who_are_we", views.who_are_we, name="who_are_we"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

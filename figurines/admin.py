from django.contrib import admin
from .models import Category, Figurine, DidYouSee

# Register your models here.
admin.site.register(Category)
admin.site.register(Figurine)
admin.site.register(DidYouSee)

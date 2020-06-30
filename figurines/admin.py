from django.contrib import admin
from .models import Category, Figurine, Collection, DidYouSee

# Register your models here.
admin.site.register(Category)
admin.site.register(Figurine)
admin.site.register(Collection)
admin.site.register(DidYouSee)

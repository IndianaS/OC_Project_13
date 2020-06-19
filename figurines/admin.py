from django.contrib import admin
from .models import Category, Figurine, Collection, Did_you_see

# Register your models here.
admin.site.register(Category)
admin.site.register(Figurine)
admin.site.register(Collection)
admin.site.register(Did_you_see)

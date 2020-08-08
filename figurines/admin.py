from django.contrib import admin
from .models import Category, Figurine, DidYouSee


# Register your models here.
class DidYouSeeAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'report',)
    list_filter = ('report',)


class FigurineAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'figurine_number',)


admin.site.register(Category)
admin.site.register(Figurine, FigurineAdmin)
admin.site.register(DidYouSee, DidYouSeeAdmin)

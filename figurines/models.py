from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name


class Figurine(models.Model):

    id = models.BigIntegerField(primary_key=True)
    id_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    picture_figurine = models.ImageField(upload_to='figurines')

    def __str__(self):
        return self.name


class Collection(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collection",
    )
    figurine = models.ForeignKey(
        Figurine,
        on_delete=models.CASCADE,
        verbose_name="Figurine enregistré"
    )


class Did_you_see(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    
    class Meta:
        verbose_name ="article"
        ordering = ['date']
    
    def __str__(self):
        return self.title

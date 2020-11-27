from django.conf import settings
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name


class Figurine(models.Model):

    figurine_number = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    picture_figurine = models.ImageField(upload_to='', null=True, blank=True)
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return repr(self.name)

class DidYouSee(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    date = models.DateField(auto_now=True, verbose_name="Date de parution")
    datetime = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        "DidYouSee",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    report = models.BooleanField(default=False)

    class Meta:
        verbose_name = "article"
        ordering = ['-datetime']

    def __str__(self):
        return self.title

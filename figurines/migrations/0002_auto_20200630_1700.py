# Generated by Django 3.0.7 on 2020-06-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figurines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figurine',
            name='picture_figurine',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
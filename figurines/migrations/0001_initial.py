# Generated by Django 3.0.8 on 2020-07-13 22:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Figurine',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('figurine_number', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                (
                    'picture_figurine',
                    models.ImageField(blank=True, null=True, upload_to=''),
                ),
                (
                    'category',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='figurines.Category',
                    ),
                ),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DidYouSee',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(null=True)),
                (
                    'date',
                    models.DateField(
                        auto_now=True, verbose_name='Date de parution'
                    ),
                ),
                ('datetime', models.DateTimeField(auto_now=True)),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'parent',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='figurines.DidYouSee',
                    ),
                ),
            ],
            options={
                'verbose_name': 'article',
                'ordering': ['-datetime'],
            },
        ),
    ]

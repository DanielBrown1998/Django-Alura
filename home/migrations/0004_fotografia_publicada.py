# Generated by Django 5.1.1 on 2024-10-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]

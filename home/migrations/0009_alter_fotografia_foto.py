# Generated by Django 5.1.1 on 2024-10-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(upload_to='fotos/%Y/%m/%d/'),
        ),
    ]
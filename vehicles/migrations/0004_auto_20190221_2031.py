# Generated by Django 2.1.7 on 2019-02-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20190221_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Zdjęcie'),
        ),
    ]
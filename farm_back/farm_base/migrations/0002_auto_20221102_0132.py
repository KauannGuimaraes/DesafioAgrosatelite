# Generated by Django 2.2 on 2022-11-02 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='municipality',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Municipality'),
        ),
        migrations.AddField(
            model_name='farm',
            name='municipio',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Municipio'),
        ),
        migrations.AddField(
            model_name='farm',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='State'),
        ),
    ]

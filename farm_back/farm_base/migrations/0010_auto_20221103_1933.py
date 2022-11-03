# Generated by Django 2.2 on 2022-11-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_base', '0009_auto_20221103_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='municipality',
            field=models.CharField(max_length=255, verbose_name='Municipality'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='state',
            field=models.CharField(max_length=255, verbose_name='State'),
        ),
    ]

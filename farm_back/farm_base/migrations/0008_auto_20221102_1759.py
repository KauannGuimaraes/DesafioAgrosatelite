# Generated by Django 2.2 on 2022-11-02 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_base', '0007_auto_20221102_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='farm_base.Owner', verbose_name='Owner'),
        ),
    ]

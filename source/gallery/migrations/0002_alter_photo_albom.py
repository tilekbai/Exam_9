# Generated by Django 3.2.3 on 2021-05-29 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='albom',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.albom'),
        ),
    ]

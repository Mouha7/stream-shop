# Generated by Django 4.2.11 on 2024-05-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='poster',
            field=models.ImageField(upload_to='serie/'),
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-07 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_alter_idnumber_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='movie/actor/images'),
        ),
    ]

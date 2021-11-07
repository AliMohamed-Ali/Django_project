# Generated by Django 3.2.9 on 2021-11-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20211106_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='banner',
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default=' ', upload_to='movie/movie/images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(upload_to='movie/movie/videos'),
        ),
    ]
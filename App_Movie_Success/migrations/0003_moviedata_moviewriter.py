# Generated by Django 3.2.12 on 2022-03-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Movie_Success', '0002_moviedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='MovieWriter',
            field=models.CharField(default=None, max_length=100),
        ),
    ]

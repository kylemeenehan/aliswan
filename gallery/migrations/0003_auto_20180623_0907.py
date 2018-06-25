# Generated by Django 2.0.6 on 2018-06-23 09:07

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180622_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(default='images/placeholders/no-image.jpg', upload_to=gallery.models.image_upload_handler),
        ),
        migrations.AlterField(
            model_name='work',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
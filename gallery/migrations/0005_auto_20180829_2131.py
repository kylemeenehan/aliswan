# Generated by Django 2.1 on 2018-08-29 19:31

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_remove_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField()),
                ('videoId', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Video',
            new_name='ArtDirecting',
        ),
        migrations.AlterField(
            model_name='photography',
            name='image',
            field=models.ImageField(default='images/placeholders/no-image.jpg', upload_to=gallery.models.photo_upload_handler),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FolderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_folder', models.CharField(max_length=200, unique=True, verbose_name='Название папки')),
                ('url_dir', models.CharField(max_length=200, verbose_name='Путь к папке')),
                ('url_video', models.CharField(max_length=200, verbose_name='Путь к видео')),
                ('url_txt', models.CharField(max_length=200, verbose_name='Путь к текстовому файлу')),
                ('url_picture', models.CharField(max_length=200, verbose_name='Путь к картинке')),
            ],
        ),
    ]

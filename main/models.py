from django.db import models


class FolderModel(models.Model):
    name_folder = models.CharField(max_length=200, verbose_name="Название папки", unique=True)
    url_dir = models.CharField(max_length=200, verbose_name="Путь к папке")
    url_video = models.CharField(max_length=200, verbose_name="Путь к видео")
    url_txt = models.CharField(max_length=200, verbose_name="Путь к текстовому файлу")
    url_picture = models.CharField(max_length=200, verbose_name="Путь к картинке")

    def __str__(self):
        return f"{self.name_folder}"

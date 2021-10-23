import os
from django.shortcuts import get_object_or_404
from main.models import FolderModel
from django_website.settings import MEDIA_ROOT


def read_file(file, start=0, end=None, offset_size=6000):
    offset_len = 0

    # смещаемся на нужный байт
    file.seek(start, 0)
    while True:
        if end:
            # определяем длину участка видео
            if offset_size < (end - start - offset_len):
                byte_length = offset_size
            else:
                byte_length = end - start - offset_len

            # если файл закончился выходим из цикла
            if byte_length <= 0:
                break
        else:
            byte_length = offset_size

        # чтение файла
        data = file.read(byte_length)
        # если файл пустой
        if not data:
            break

        # продолжаем чтение файла
        offset_len += byte_length
        yield data


def open_read_video(request_range, video_pk):
    video = get_object_or_404(FolderModel, pk=video_pk)
    url_video = f"{MEDIA_ROOT}{video.url_dir}/{video.url_video}"

    file_bytes = open(url_video, 'rb')
    # получение размера видео
    file_size = os.path.getsize(url_video)

    content_length = file_size
    # начальная точка
    status_code = 200

    if request_range is not None:
        # получение размер контента bytes
        content_ranges = request_range.strip().split('=')[-1]

        # получаем первую и последню позицию
        start_point = content_ranges.split('-')[0]
        end_point = content_ranges.split('-')[1]

        end_point = int(end_point) if end_point else file_size - 1
        start_point = int(start_point) if start_point else 0

        # длина контента
        content_length = (end_point - start_point) + 1
        # итератор из файла
        file_bytes = read_file(file_bytes, start=start_point, end=end_point + 1)

        status_code = 206  # 206 Partial Content
        request_range = f'bytes {start_point}-{end_point}/{file_size}'

    return status_code, request_range, content_length, file_bytes

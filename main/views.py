from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from django_website.settings import MEDIA_ROOT
from main.models import FolderModel
from main.utils import open_read_video


# парсинг файл
def open_txt_file(file):
    with open(file, 'r') as f:
        res = []
        for line in f.readlines()[1:]:
            time = line.rstrip('\n').split(',')
            try:
                float(time[2])
                res.append(time)
            except BaseException:
                pass
    return res

# рендер страницы
def get_folder(request, pk=None):
    all_folder = FolderModel.objects.all()
    context = {"object_list": all_folder}
    if pk is not None:
        obj_folder = get_object_or_404(FolderModel, pk=pk)
        pictures = f"/media{obj_folder.url_dir}/{obj_folder.url_picture}"
        txt_file = f'{MEDIA_ROOT}{obj_folder.url_dir}/{obj_folder.url_txt}'
        list_time = open_txt_file(txt_file)
        context.update({"object": obj_folder, "time_code": list_time, "url_pictures": pictures})

        return render(request, 'main/main_folder.html', context)

    return render(request, 'main/base.html', context)


def get_video(request, pk):
    # получение заголовка запроса Range
    request_range = request.headers.get('range')

    status_code, response_range, content_length, file_bytes = open_read_video(request_range, pk)

    # ответ от сервера
    response = StreamingHttpResponse(file_bytes, status=status_code, content_type='video/mp4')

    # отправка заголовка: размер файла, кусок видео в байтах, размер файла
    response['Content-Range'] = response_range
    response['Content-Length'] = str(content_length)
    response['Accept-Ranges'] = 'bytes'
    return response
from django.core.management.base import BaseCommand
from main.models import FolderModel

FOLDER_DATA = [{"name_folder": 'Folder_1', "url_dir": "/files/1", "url_video": "video.mp4",
                "url_txt": "labels.txt", "url_picture": "pic.png"},
               {"name_folder": 'Folder_2', "url_dir": "/files/2", "url_video": "video.mp4",
                "url_txt": "labels.txt", "url_picture": "pic.png"},
               {"name_folder": 'Folder_3', "url_dir": "/files/3", "url_video": "video.mp4",
                "url_txt": "labels.txt", "url_picture": "pic.png"},
               {"name_folder": 'Folder_6', "url_dir": "/files/6", "url_video": "video.mp4",
                "url_txt": "labels.txt", "url_picture": "pic.png"},
               {"name_folder": 'Folder_8', "url_dir": "/files/8", "url_video": "video.mp4",
                "url_txt": "labels.txt", "url_picture": "pic.png"},
               {"name_folder": 'Folder_9', "url_dir": "/files/9", "url_video": "video.mp4",
                "url_txt": "labels.txt", "url_picture": "pic.png"},
               ]


class Command(BaseCommand):
    def handle(self, *args, **options):
        FolderModel.objects.all().delete()

        for item in FOLDER_DATA:
            obj= FolderModel(
                name_folder=item["name_folder"], url_dir=item["url_dir"],
                url_video=item["url_video"], url_txt=item["url_txt"], url_picture=item["url_picture"]
            )
            obj.save()
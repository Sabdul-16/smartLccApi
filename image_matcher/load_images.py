import os
from pathlib import Path
import django
from django.core.files import File
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_matcher.settings')
django.setup()

from image_app.models import ImageModel  # NOQA

IMG_DIR = Path('G:/LCC_ProjectFinal/')  # update this to your images directory
IMG_FILES = ['Color1.png', 'Color2.png', 'Color3.png', 'Color4.png']  # update this to your image file names


def load_images_to_db():
    for i, img in enumerate(IMG_FILES, start=1):
        file_path = IMG_DIR / img
        with open(file_path, 'rb') as img_file:
            ImageModel.objects.create(index=i, image=File(img_file, name=img))


if __name__ == '__main__':
    load_images_to_db()

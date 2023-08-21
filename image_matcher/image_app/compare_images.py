from PIL import Image
from .models import ImageModel
import skimage
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize
import numpy as np


def compare_images(image_file):
    input_image = Image.open(image_file).convert('RGB')
    best_fit_index = -1
    max_ssim = -1

    for image_model in ImageModel.objects.all():
        image = Image.open(image_model.image.path).convert('RGB')
        ref_image = skimage.color.rgb2gray(np.array(input_image))
        image = skimage.color.rgb2gray(np.array(image))
        image = resize(image, ref_image.shape)
        similarity = ssim(ref_image, image, data_range=1.0)

        if similarity > max_ssim:
            max_ssim = similarity
            best_fit_index = image_model.index

    return best_fit_index if max_ssim != -1 else 100

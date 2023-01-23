from django.db import models
from PIL import Image as PILImage

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=50, default=None)
    file = models.ImageField(blank=False, width_field='width', height_field='height')
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)


    # def save(self, *args, **kwargs):
    #     """
    #     https://stackoverflow.com/questions/57111648/how-to-resize-an-imagefield-image-before-saving-it-in-python-django-model
    #
    #     super(Image, self).save(*args, **kwargs)
    #     imag = PILImage.open(self.img.path)
    #     if imag.width > 400 or imag.height > 300:
    #         output_size = (400, 300)
    #         imag.thumbnail(output_size)
    #         imag.save(self.post_image.path)
    #     """
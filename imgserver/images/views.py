from .models import Image
from rest_framework import generics, mixins
from .serializers import ImageSerializer
from django.shortcuts import render
from PIL import Image as PILimage
from django.core.files.uploadedfile import InMemoryUploadedFile, UploadedFile

class ImageMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'pk'


    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def perform_create(self, serializer):
        # request = serializer.context['request']
        # _file = request.FILES['file']
        #
        # _width = int(serializer.initial_data['width'])
        # _height = int(serializer.initial_data['height'])
        #
        # print('height ', _height)
        #
        # _image = PILimage.open(_file)
        # _image = _image.resize((_width, _height), PILimage.ANTIALIAS)
        #
        # print(_file.__dict__, type(_file))
        # buffer = BytesIO()
        #
        # _image.save(buffer, format='JPEG')
        # buffer.seek(0)
        #
        #
        # x = serializer.context['request'].FILES['file'] = InMemoryUploadedFile(buffer, 'file', _file.name, 'image/jpeg', _image.size, 'utf-8')
        # print(x.__dict__)
        serializer.save()

    def filter_queryset(self, queryset):
        if 'title' in self.request.data:
            substring = self.request.data['title']
            return self.queryset.filter(title__icontains=substring)
        return super().filter_queryset(queryset)




image_mixin_view = ImageMixinView.as_view()
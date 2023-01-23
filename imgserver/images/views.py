from .models import Image
from rest_framework import generics, mixins
from .serializers import ImageSerializer
from django.shortcuts import render
from PIL import Image as PILimage
from django.core.files.uploadedfile import InMemoryUploadedFile, UploadedFile

class ImageMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    # queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'pk'


    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get_queryset(self):
    #     queryset = Image.objects.all()
    #     title_param = self.request.query_params.get('title')
    #     if title_param is not None:
    #         return self.queryset.filter(title__icontains=title_param)
    #     elif 'title' in self.request.data:
    #         substring = self.request.data['title']
    #         return self.queryset.filter(title__icontains=substring)
    #     else:
    #         return queryset

    # def filter_queryset(self, queryset):
    #     if 'title' in self.request.data:
    #         substring = self.request.data['title']
    #         return self.queryset.filter(title__i
    #         contains=substring)
    #     return super().filter_queryset(queryset)

    def get_queryset(self):
        queryset = Image.objects.all()
        return queryset

    def filter_queryset(self, queryset):
        title_param = self.request.query_params.get('title')
        if title_param is not None:
            return queryset.filter(title__icontains=title_param)
        elif 'title' in self.request.data:
            substring = self.request.data['title']
            return queryset.filter(title__icontains=substring)
        else:
            return queryset


image_mixin_view = ImageMixinView.as_view()
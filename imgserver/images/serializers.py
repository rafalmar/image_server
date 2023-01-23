import sys
from .models import Image
from rest_framework import serializers
from PIL import Image as PILimage
from io import BytesIO


class ImageSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(required=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'file', 'width', 'height']

    def create(self, validated_data):
        uploaded_file = validated_data['file']

        image = PILimage.open(uploaded_file.file)
        width, height = image.size

        new_width = validated_data.get('width', width)
        new_height = validated_data.get('height', height)

        new_width = new_width if new_width else width
        new_height = new_height if new_height else height

        image = image.resize((new_width, new_height), PILimage.ANTIALIAS)
        buffer = BytesIO()
        image.save(buffer, format=uploaded_file.image.format)
        buffer.seek(0)

        uploaded_file.file = buffer
        uploaded_file.image = image
        uploaded_file.size = sys.getsizeof(buffer)

        validated_data['file'] = uploaded_file

        return super().create(validated_data)



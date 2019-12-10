from rest_framework import serializers
from admin_launcher.models import *

# Serializers define the API representation.
class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = background
        fields = ['nombre', 'descripcion', 'imagen', 'activo']


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = ['en', 'es']

class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = ['en', 'es']

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['en', 'es']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class AppSerializer(serializers.ModelSerializer):

    title = TitleSerializer(many=False, read_only=True)
    description = DescriptionSerializer(many=False, read_only=True)
    trailer = TrailerSerializer(many=False, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    #images = serializers.StringRelatedField(many=True)

    class Meta:
        model = App
        fields = ['name','skip','start','end','year','package','uri','title','description','trailer','banner','logo','images']


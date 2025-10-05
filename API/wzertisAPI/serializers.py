# serializers.py
from rest_framework import serializers
from .models import AuthorInfo, ArtGroup, Artwork, Appeal

class AuthorInfoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)

    class Meta:
        model = AuthorInfo
        fields = '__all__'  # или перечислите: ['id', 'name', 'bio', 'email']

class ArtGroupSerializer(serializers.ModelSerializer):
    queryset = ArtGroup.objects.all()

    class Meta:
        model = ArtGroup
        fields = '__all__'

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'

class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'

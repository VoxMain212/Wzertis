from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from .models import AuthorInfo, ArtGroup, Artwork, Appeal
from .serializers import AuthorInfoSerializer, ArtGroupSerializer, ArtworkSerializer, AppealSerializer


def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def author_info_api(request):
    author = AuthorInfo.objects.first()
    if author:
        serializer = AuthorInfoSerializer(author)
        return Response(serializer.data)
    else:
        return Response({"error": "Информация об авторе не найдена"}, status=404)
    

@api_view(['GET'])
def get_groups(request):
    groups = ArtGroup.objects.all()
    if groups:
        serializer = ArtGroupSerializer(groups, many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "Информация о группах не найдена"}, status=404)
    
@api_view(['GET'])
def get_artworks(request):
    artworks = Artwork.objects.all()
    if artworks:
        serializer = ArtworkSerializer(artworks, many=True)
        return Response(serializer.data)
    return Response({'error': 'Информация о работах не найдена'}, status=404)

@api_view(['GET'])
def get_fav_artworks(request):
    artworks = Artwork.objects.filter(favorite=True)
    if artworks:
        serializer = ArtworkSerializer(artworks, many=True)
        return Response(serializer.data)
    return Response({'error': 'Не найдена информация о избранных работах'})

@api_view(['GET'])
def get_group_by_id(request, group_id):
    group = get_object_or_404(ArtGroup, id=group_id)
    serializer = ArtGroupSerializer(group)
    return Response(serializer.data)

@api_view(['POST'])
def send_appeal(request):
    serializer = AppealSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)
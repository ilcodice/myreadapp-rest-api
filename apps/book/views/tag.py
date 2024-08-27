from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Tag
from apps.book.serializer import TagSerializer


@api_view(['GET']) #define our http
def list_tags(request):
    # Get all tags using ORM
    tags = Tag.objects.all()
    # Deserialize using the TagSerializer
    data = TagSerializer(tags, many=True)
    # Return data
    return Response(data.data, status=status.HTTP_200_OK)
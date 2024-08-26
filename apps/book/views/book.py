from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Book, Author
from apps.book.serializer import ReadBookSerializer , CreateBookSerializer


# List book
@api_view(['GET'])
def list_book(request):
    books = Book.objects.all()

    data = ReadBookSerializer(books, many=True)

    return Response(data.data, status=status.HTTP_200_OK)


# create book
@api_view(['POST'])
def create_book(request):
    with transaction.atomic():
        data = request.data  # retrive data from body
        authors = data['authors']   # retrive the authors

        book = CreateBookSerializer(data=data)  # serialize the data

        book.is_valid()
        saved_book = book.save()    # if its valid then save

        #Add authors

        for author in authors:  # add author manually 
            author_obj = Author.objects.get(pk=author['id']) # getting author object from the id 
            saved_book.authors.add(author_obj, through_defaults={'role': author['role']}) # add author object to author atribute

    # Return a JSON transformed data 
    return Response({'isbn': saved_book.isbn}, status=status.HTTP_201_CREATED)
    
    #return Response({'detail': 'Invalid request data', 'error':'Invalid_Resquest'}, status=status.HTTP_400_BAD_REQUEST)

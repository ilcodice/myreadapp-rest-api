# list Book -> 
#Create 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apps.book.models import Book,Author
from apps.book.serializer import ReadBookSerializer,CreateBookSerializer
from django.db import transaction


@api_view(['GET'])
def list_books(request):

    books = Book.objects.all()
    
    data = ReadBookSerializer(books, many=True)
    # Return data
    return Response(data.data, status=status.HTTP_200_OK)



@api_view(['POST'])
def create_books(request):
    with transaction.atomic():
        data = request.data
        authors = data['authors']


        book = CreateBookSerializer(data=data)

        book.is_valid()
        saved_book = book.save()

            #add authors
        for author in authors:
            author_obj = Author.objects.get(pk=author['id'])
            saved_book.authors.add(author_obj, through_defaults={'role':author['role']})

        # returns json transformed data
    return Response({'isbn':saved_book.isbn},status=status.HTTP_201_CREATED)
    
    #return Response({'detail': 'Invalid request data','error' : 'Invalid request'},status=status.HTTP_400_BAD_REQUEST)



class BooksView(APIView):
    #GET 
    def get(self,request):
        #get all data from book
        books = Book.objects.all()

        #deserialization
        data = ReadBookSerializer(books,many = True)

        #Retrun Json
        return Response({'data' : data.data},status= status.HTTP_200_OK)

    #post    
    def post(self,request):
        pass


    #Delete
    def delete(self,request):
        pass

    #put
    def put(self,request):
        pass

    #patch
    def patch(self,request):
        pass     
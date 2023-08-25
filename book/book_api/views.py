from django.shortcuts import render
from rest_framework.response import Response
from book_api.models import Book
from rest_framework.decorators import api_view
from book_api.serializer import BookSerializer
from rest_framework import status


@api_view(["GET"])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def book_get_pk(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except:
        return Response(
            {'error': 'Book does not exists'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def book_put_pk(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(
            {'error': 'provided field does not exists'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def book_delete_pk(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({'results': 'record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(
            {'error': 'Book does not exists'}, status=status.HTTP_404_NOT_FOUND)

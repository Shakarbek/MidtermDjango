from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from main.models import Book, Journal
from main.serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


    @action(methods=['GET'], detail=False, url_path='inactive', url_name='in_active', permission_classes=(AllowAny,))
    def not_active(self, request):
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class AuthorApiView(generics.RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
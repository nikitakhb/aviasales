from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.utils.translation import gettext_lazy as _

from rest_framework.serializers import ListSerializer, CharField

from anagram.serializers import WordListSerializer
from anagram.models import Word


class LoadWordsView(GenericViewSet):

    queryset = Word.objects
    serializer_class = WordListSerializer

    @swagger_auto_schema(
        operation_description=_('Загрузка списка'),
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        words = [Word(word=word) for word in serializer.data]
        Word.objects.bulk_create(words, ignore_conflicts=True)
        return Response(status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description=_('Очистка списка'),
    )
    @action(detail=False, methods=['delete'], url_path='delete')
    def clear(self, request):
        Word.objects.all().delete()
        return Response(status=status.HTTP_200_OK)


class FindAnagramView(GenericViewSet):

    queryset = Word.objects

    @swagger_auto_schema(
        operation_description=_('Получения аннаграм из загруженного списка'),
        manual_parameters=[
            openapi.Parameter(
                name='word',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description=_('Слово для поиска'),
            ),
        ],
        responses={
            status.HTTP_200_OK: ListSerializer(child=CharField()),
            status.HTTP_404_NOT_FOUND: None,
        }
    )
    def list(self, request, *args, **kwargs):
        query_word = request.query_params.get('word', None)
        if query_word:
            obj = Word(word=query_word)
            words = self.get_queryset().filter(hash=obj.hash).values_list('word', flat=True).all()
            if words:
                return Response(data=words, status=status.HTTP_200_OK)
        return Response(data=None, status=status.HTTP_404_NOT_FOUND)

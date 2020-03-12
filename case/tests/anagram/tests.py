import pytest

from rest_framework.reverse import reverse
from rest_framework import status

from anagram.models import Word


@pytest.mark.django_db
def test_create_list(client, create_list_word):
    response = client.post(
        reverse('load-list'),
        data=create_list_word,
        format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert set(Word.objects.values_list('word', flat=True).all()) == set(create_list_word)


@pytest.mark.django_db
def test_delete_list(client, create_words):
    assert Word.objects.count() == 100
    response = client.delete(
        reverse('load-clear')
    )
    assert response.status_code == status.HTTP_200_OK
    assert Word.objects.count() == 0


@pytest.mark.django_db
def test_get_word(client, create_words):
    word = Word.objects.first()
    print(f"{reverse('find-list')}?word={word.word}")
    response = client.get(
        f"{reverse('find-list')}?word={word.word}"
    )
    words = Word.objects.filter(hash=word.hash).values_list('word', flat=True).all()

    assert response.status_code == status.HTTP_200_OK

    response_word = response.data

    assert len(words) == len(response_word)
    assert set(words) == set(response_word)






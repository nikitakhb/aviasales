import random
import pytest
import string
from anagram.models import Word
from rest_framework.test import APIClient


@pytest.fixture()
def create_words():
    words = [
        Word(
            word=''.join(random.choices(string.ascii_letters , k=20))
        )
        for _ in range(100)
    ]
    return Word.objects.bulk_create(words)


@pytest.fixture()
def create_list_word():
    words = [
        ''.join(random.choices(string.ascii_letters, k=20))
        for _ in range(100)
    ]
    return words


@pytest.fixture()
def client():
    return APIClient()

from django.db import models
from django.utils.translation import gettext_lazy as _

from anagram.use_case import get_chars_from_word
from hashlib import sha256


class Word(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.word and not self.hash:
            has = self.calc_hash()
            self.hash = has

    word = models.CharField(
        _('Слово'),
        unique=True,
        max_length=1024,
        primary_key=True
    )

    hash = models.CharField(
        _('Хеш-слова'),
        max_length=64
    )

    def calc_hash(self):
        word = self.word
        chars = ''.join([f'{char.lower()}{count}' for char, count in sorted(get_chars_from_word(word).items(), key=lambda x: x[0])])
        return sha256(chars.encode()).hexdigest()

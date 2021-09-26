from typing import Iterable

from WordProcessor import WordTokenizer


class CharacterTokenizer(WordTokenizer):
    def tokenize(self, content: str) -> Iterable[str]:
        return content.__iter__()

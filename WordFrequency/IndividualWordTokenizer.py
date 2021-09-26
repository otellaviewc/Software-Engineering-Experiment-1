import re
from typing import Iterable

from WordProcessor import WordTokenizer


class IndividualWordTokenizer(WordTokenizer):
    def tokenize(self, content: str) -> Iterable[str]:
        word_pattern = re.compile(r'[a-z]+\d*')
        return word_pattern.findall(content.lower())

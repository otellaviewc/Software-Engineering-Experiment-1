from collections import Counter
from typing import Iterable, List, Tuple

from WordProcessor import WordCounter


class IndividualWordCounter(WordCounter):
    def count(self, tokens: Iterable[str]) -> List[Tuple[str, int]]:
        word_counts = Counter(tokens)
        return word_counts.most_common(100)

from abc import ABC, abstractmethod
from typing import Optional, List, Tuple, Iterable
from operator import itemgetter


class WordLoader(ABC):
    @abstractmethod
    def load(self) -> str:
        pass


class WordTokenizer(ABC):
    @abstractmethod
    def tokenize(self, content: str) -> Iterable[str]:
        pass


class WordCounter(ABC):
    @abstractmethod
    def count(self, tokens: Iterable[str]) -> List[Tuple[str, int]]:
        pass


class WordProcessor:
    def __init__(self):
        self._loader: Optional[WordLoader] = None
        self._tokenizer: Optional[WordTokenizer] = None
        self._counter: Optional[WordCounter] = None

    def set_loader(self, loader: WordLoader):
        self._loader = loader

    def set_tokenizer(self, tokenizer: WordTokenizer):
        self._tokenizer = tokenizer

    def set_counter(self, counter: WordCounter):
        self._counter = counter

    def summary(self) -> str:
        content = self._loader.load()
        tokens = self._tokenizer.tokenize(content)
        counts = self._counter.count(tokens)

        counts.sort(key=itemgetter(1, 0), reverse=True)

        total = sum(count for _, count in counts)

        return '\n'.join(map(lambda x: f'{x[0]}\t{x[1] / total * 100 :.2f}%', counts))

from typing import Iterable, List, Tuple

from WordProcessor import WordCounter


ORD_A = ord('a')
ORD_Z = ord('z')

ORD_UA = ord('A')
ORD_UZ = ord('Z')


class CharacterCounter(WordCounter):
    def count(self, tokens: Iterable[str]) -> List[Tuple[str, int]]:
        counts = [0 for _ in range(26)]

        for ch in map(lambda x: ord(x), tokens):
            if ORD_A <= ch <= ORD_Z:
                counts[ch - ORD_A] += 1
            elif ORD_UA <= ch <= ORD_UZ:
                counts[ch - ORD_UA] += 1

        return [(chr(ORD_A + i), count) for i, count in enumerate(counts)]

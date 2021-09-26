from WordProcessor import WordProcessor


class WordFrequency:
    def __init__(self):
        self._word_processor = WordProcessor()

    def _c(self, file: str) -> 'WordFrequency':
        """
        输出某个英文文本文件中 26 字母出现的频率，由高到低排列，并显示字母出现的百分比，精确到小数点后面两位。

        :param file: 待统计文本文件路径。
        """
        from SingleFileLoader import SingleFileLoader
        from CharacterTokenizer import CharacterTokenizer
        from CharacterCounter import CharacterCounter

        self._word_processor.set_loader(SingleFileLoader(file))
        self._word_processor.set_tokenizer(CharacterTokenizer())
        self._word_processor.set_counter(CharacterCounter())
        return self

    def _f(self, file: str) -> 'WordFrequency':
        """
        输出单个文件中的前 N 个最常出现的英语单词，结合 -d -s -n -x -v 参数使用。

        :param file: 待统计文本文件路径。
        """
        from SingleFileLoader import SingleFileLoader
        from IndividualWordTokenizer import IndividualWordTokenizer
        from IndividualWordCounter import IndividualWordCounter

        self._word_processor.set_loader(SingleFileLoader(file))
        self._word_processor.set_tokenizer(IndividualWordTokenizer())
        self._word_processor.set_counter(IndividualWordCounter())
        return self

    def _d(self, directory: str) -> 'WordFrequency':
        """
        指定文件目录，对目录下每一个文件执行 wf.exe -f 的操作。

        :param directory: 文件目录。
        """
        return self

    def _s(self) -> 'WordFrequency':
        return self

    def _n(self) -> 'WordFrequency':
        return self

    def _x(self, stop_words: str) -> 'WordFrequency':
        """
        停词表。

        :param stop_words: 停词表文件路径。
        """
        return self

    def _p(self) -> 'WordFrequency':
        """
        统计短语数量，按照出现频率排列。同一频率的词组，按照字典序来排列。
        """
        return self

    def _v(self, verb_words: str) -> 'WordFrequency':
        """
        把动词形态都统一之后再计数。
        """
        return self

    def __str__(self) -> str:
        return self._word_processor.summary()

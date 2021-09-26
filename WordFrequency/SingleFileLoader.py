import re

from WordProcessor import WordLoader


class SampleLoader(WordLoader):
    def __init__(self, content: str):
        self._content = content

    def load(self) -> str:
        return self._content


class SingleFileLoader(WordLoader):
    def __init__(self, file_name: str):
        self._file_name = file_name

    def load(self) -> str:
        special_characters_pattern = re.compile(r"(\\x[1-9a-f]{2})|(\\[a-z])")

        with open(self._file_name, mode='rb') as file:
            raw_content = str(file.read())

            content = re.sub(special_characters_pattern, '', raw_content)

            return content

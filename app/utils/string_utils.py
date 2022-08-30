from app.constant import Constant
from config.config import settings


class Acronym:
    """Implements the logic of generating acronym."""

    def __init__(self, acronym_ignore=settings.acronym_ignore):
        self.acronym_ignore = acronym_ignore

    def acronymize(self, sentence: str) -> str:
        """Converts string into its acronym."""
        for word in self.acronym_ignore:
            sentence = sentence.replace(word, '')
        acc = ""
        for word in sentence.split():
            # if the word is already an acronym
            # we take the whole acronym
            # ex: ITMO University -> ITMOU
            if word == word.upper():
                acc += word
            else:
                acc += word[0].upper()
        # if the acronym is greater than 6 char
        # we shrink the acronym by taking only the first and last char
        if len(acc) > Constant.ACC_MAX_LEN:
            acc = acc[0] + acc[-1]
        return acc


class StringSlicer:
    """Implements the logic for truncating strings."""

    def __init__(self, max_len=settings.max_name_len):
        self.max_len = max_len

    def slice(self, string: str) -> str:
        """Returns string to appropriate size."""
        if len(string) > self.max_len:
            string = self.__generate_appropriate_size_string(string)

        return string[:self.max_len]

    def __generate_appropriate_size_string(self, string):
        """Generates appropriate size string."""
        tokens = string.split()
        if len(tokens) == 1:
            return string

        final_string = ""
        for token in tokens:
            if len(token) + len(final_string) < self.max_len:
                final_string += token + " "

        return final_string.strip()

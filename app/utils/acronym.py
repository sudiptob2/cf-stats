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
        return acc

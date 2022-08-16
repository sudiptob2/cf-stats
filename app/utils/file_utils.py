import os
from collections import namedtuple

from app.constant import Constant

FileContext = namedtuple('FileContext', ['svg', 'filename'])
Config = namedtuple('Config', ['badge_type'])


class FileHelper:
    """Provides methods for R/W files."""

    @classmethod
    def create_folder(cls):
        """Create the output folder if it does not already exist."""
        if not os.path.isdir(Constant.OUTPUT_FOLDER):
            os.mkdir(Constant.OUTPUT_FOLDER)

    @classmethod
    def save_svg(cls, file_context: FileContext):
        """Saves the given svg into the output folder."""
        cls.create_folder()
        with open(file_context.filename, 'w') as f:
            f.write(file_context.svg)


if __name__ == '__main__':
    FileHelper.create_folder()

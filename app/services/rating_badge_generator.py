import re

import pybadges

from app.constant import Constant
from app.models.user import User
from app.services.generator_interface import IGenerator
from app.utils.file_utils import FileHelper, FileContext, Config


class BadgeGenerator(IGenerator, FileHelper):

    @classmethod
    def generate(cls, config: Config):
        """Generate svg badge for rating."""
        user = User()
        with open(f'{Constant.TEMPLATE_FOLDER}/rating_template.svg', 'r') as f:
            output = f.read()

        output = re.sub('{{ codeforces }}', Constant.CODEFORCES, output)
        output = re.sub('{{ rating }}', str(getattr(user, config.badge_type)), output)
        output = re.sub('#123456', str(user.rating_color) if config.badge_type == 'rating' else str(user.max_rating_color), output)
        file_context = FileContext(output, f"{Constant.OUTPUT_FOLDER}/{config.badge_type}.svg")
        cls.save_svg(file_context)
        return output

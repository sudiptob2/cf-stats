import re

from app.constant import Constant
from app.models.user import User
from app.services.generator_interface import IGenerator
from app.utils.file_utils import FileHelper, FileContext, Config


class CardGenerator(IGenerator, FileHelper):

    @classmethod
    def generate(cls, config: Config):
        """Generate svg badge for rating."""
        user = User()
        card = cls._get_card_svg(config)
        file_context = FileContext(card, f"{Constant.OUTPUT_FOLDER}/{config.badge_type}.svg")
        cls.save_svg(file_context)
        return card

    @classmethod
    def _get_card_svg(cls, config: Config) -> str:
        """Generates svg card according to the config."""
        user = User()
        with open(f'{Constant.TEMPLATE_FOLDER}/stat_card.svg', 'r') as f:
            output = f.read()

        output = re.sub('{{ name }}', user.sliced_name, output)
        if not user.org_acronym:
            output = re.sub('{{ organization }} \|', user.org_acronym, output)
        else:
            output = re.sub('{{ organization }}', user.org_acronym, output)
        output = re.sub('{{ rating }}', user.rank, output)
        output = re.sub('green', user.rating_color, output)
        output = re.sub('{{ max }}', user.max_rank, output)
        output = re.sub('#03A89E', user.max_rating_color, output)
        output = re.sub('{{ year }}', str(user.member_since), output)
        output = re.sub('{{ contest_rating }}', str(user.rating), output)
        output = re.sub('{{ max_rating }}', str(user.max_rating), output)
        output = re.sub('{{ contests }}', str(user.contests), output)
        output = re.sub('{{ accepted }}', str(user.accepted), output)
        output = re.sub('{{ wrong_answers }}', str(user.wrong_ans), output)
        output = re.sub('{{ contributions }}', str(user.contributions), output)
        return output

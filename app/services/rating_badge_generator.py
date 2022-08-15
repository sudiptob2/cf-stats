import pybadges

from app.constant import Constant
from app.models.user import User
from app.services.generator_interface import IGenerator
from app.utils.file_utils import FileHelper, FileContext


class RatingBadgeGenerator(IGenerator, FileHelper):

    @classmethod
    def generate(cls):
        """Generate svg badge for rating."""
        user = User()
        badge = pybadges.badge(
            left_text=Constant.CODEFORCES,
            logo=Constant.LOGO,
            right_text=str(user.rating),
            right_color=str(user.rating_color)
        )
        file_context = FileContext(badge, f"{Constant.OUTPUT_FOLDER}/{Constant.RATING_BADGE}.svg")
        cls.save_svg(file_context)
        return badge

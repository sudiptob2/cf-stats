import requests

from config.config import settings
from app.constant import Constant


class CFRequestHandler:
    """Provides utils for requesting codeforces API."""

    user_info: dict = None
    user_submission: dict = None
    rating_changes: dict = None

    @classmethod
    def __get_user_info(cls):
        """Gets data from codeforces user.info api."""
        url = Constant.USER_INFO.format(settings.cf_handle)
        try:
            response = requests.get(url)
        except Exception:
            raise SystemExit('Could not connect to the codeforces API')
        cls.user_info = response.json().get('result')[0]

    @classmethod
    def __get_user_sub(cls):
        """Gets data from codeforces user.status api."""
        url = Constant.USER_STATUS.format(settings.cf_handle)
        try:
            response = requests.get(url)
        except Exception:
            raise SystemExit('Could not connect to the codeforces API')
        cls.user_submission = response.json().get('result')

    @classmethod
    def __get_rating_changes(cls):
        """Gets all rating changes from codeforces api."""
        url = Constant.USER_RATING.format(settings.cf_handle)
        try:
            response = requests.get(url)
        except Exception:
            raise SystemExit('Could not connect to the codeforces API')
        cls.rating_changes = response.json().get('result')

    @staticmethod
    def make_request():
        """Makes all the necessary requests to cf API."""
        CFRequestHandler.__get_user_info()
        CFRequestHandler.__get_user_sub()
        CFRequestHandler.__get_rating_changes()

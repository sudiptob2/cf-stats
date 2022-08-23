from collections import defaultdict

from app.models.user import User
from app.services.cf_request_handler import CFRequestHandler


class CFResponseParser:
    """Parse responses of codeforces API."""

    @staticmethod
    def parse():
        """Parse and make user object."""
        CFRequestHandler.make_request()
        CFResponseParser._parse_user_info(CFRequestHandler.user_info)
        CFResponseParser._parse_user_submission(CFRequestHandler.user_submission)
        CFResponseParser._parse_rating_changes(CFRequestHandler.rating_changes)

    @classmethod
    def _parse_user_info(cls, user_info):
        """Parse and sets user's basic profile."""
        user = User()
        user.name = user_info.get('firstName', '') + ' ' + user_info.get('lastName', '')
        user.organization = user_info.get('organization', '')
        user.rating = user_info.get('rating', 0)
        user.rank = user_info.get('rank', 'newbie')
        user.max_rating = user_info.get('maxRating', 0)
        user.max_rank = user_info.get('maxRank', 'newbie')
        user.contributions = user_info.get('contribution', 0)
        user.registration_unix_time = user_info.get('registrationTimeSeconds', 0)

    @classmethod
    def _parse_user_submission(cls, user_submission):
        """Parse and save submission related details."""
        user = User()
        user.submissions = len(user_submission)
        freq = defaultdict(lambda: 0)
        for sb in user_submission:
            freq[sb['verdict']] += 1

        user.accepted = freq['OK']
        user.wrong_ans = freq['WRONG_ANSWER']
        user.tle = freq['TIME_LIMIT_EXCEEDED']

    @classmethod
    def _parse_rating_changes(cls, rating_changes):
        """Sets total number of contests participated by the user."""
        user = User()
        user.contests = len(rating_changes)


if __name__ == '__main__':
    CFResponseParser.parse()
    test_user = User()
    print(test_user)

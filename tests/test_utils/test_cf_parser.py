from app.models.user import User
from app.utils.cf_response_parser import CFResponseParser


class TestCFParser:
    """Class for testing codeforces request parser methods."""

    def test_parse_user_info(self, user_info):
        """Tests CFResponseParser.make_request."""
        CFResponseParser.__parse_user_info(user_info)
        user = User()
        assert user.name == 'Dmitriy Khodyrev'

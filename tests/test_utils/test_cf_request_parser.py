from app.models.user import User
from app.services.cf_request_handler import CFRequestHandler
from app.services.cf_response_parser import CFResponseParser


class TestCFReqParser:
    """Class for testing codeforces request parser."""

    def test_parse_response(self, mocker, user_info, user_submission, rating_changes):
        """Tests CFResponseParser.parse_response."""
        user = User()

        def fake_make_request():
            CFRequestHandler.user_info = user_info
            CFRequestHandler.user_submission = user_submission
            CFRequestHandler.rating_changes = rating_changes

        mocker.patch.object(CFRequestHandler, 'make_request', fake_make_request)
        CFResponseParser.parse()

        assert user.rating == user_info.get('rating')
        assert user.submissions == len(user_submission)
        assert user.contests == len(rating_changes)

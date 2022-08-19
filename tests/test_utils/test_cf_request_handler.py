import pytest

from app.constant import Constant
from app.services.cf_request_handler import CFRequestHandler


class TestCFReqHandler:
    """Class for testing codeforces request handlers."""

    def test_make_request(self, mocker, user_info, user_submission, rating_changes):
        """Tests CFRequestHandler.make_request."""

        def fake_get_user_info():
            CFRequestHandler.user_info = user_info

        def fake_get_user_sub():
            CFRequestHandler.user_submission = user_submission

        def fake_rating_changes():
            CFRequestHandler.rating_changes = rating_changes

        mocker.patch.object(CFRequestHandler, '_get_user_info', fake_get_user_info)
        mocker.patch.object(CFRequestHandler, '_get_user_sub', fake_get_user_sub)
        mocker.patch.object(CFRequestHandler, '_get_rating_changes', fake_rating_changes)
        CFRequestHandler.make_request()
        assert type(CFRequestHandler.user_info) == dict
        assert type(CFRequestHandler.user_submission) == list
        assert type(CFRequestHandler.user_submission) == list

    def test_make_request_invalid(self):
        """Tests CFRequestHandler.make_request."""
        with pytest.raises(SystemExit):
            Constant.USER_INFO = 'https://somedsdfdf.com'
            CFRequestHandler.make_request()

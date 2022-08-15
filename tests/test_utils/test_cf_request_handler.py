import pytest

from app.constant import Constant
from app.utils.cf_request_handler import CFRequestHandler


class TestCFReqHandler:
    """Class for testing codeforces request handlers."""

    def test_make_request(self):
        """Tests CFRequestHandler.make_request."""
        CFRequestHandler.make_request()

        assert CFRequestHandler.user_info is not None
        assert CFRequestHandler.user_submission is not None
        assert CFRequestHandler.user_submission is not None

    def test_make_request_invalid(self):
        """Tests CFRequestHandler.make_request."""
        with pytest.raises(SystemExit):
            Constant.USER_INFO = 'https://somedsdfdf.com'
            CFRequestHandler.make_request()

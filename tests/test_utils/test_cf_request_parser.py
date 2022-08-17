import pytest

from app.constant import Constant
from app.services.cf_request_handler import CFRequestHandler


class TestCFReqHandler:
    """Class for testing codeforces request handlers."""

    def test_make_request(self, mocker):
        """Tests CFRequestHandler.make_request."""

        def fake_get_user_info():
            user_info = {
                "lastName": "Baral",
                "country": "Bangladesh",
                "lastOnlineTimeSeconds": 1660390665,
                "city": "Barisal",
                "rating": 1260,
                "friendOfCount": 33,
                "titlePhoto": "https://cdn-userpic.codeforces.com/306652/title/56b93861b144ce5d.jpg",
                "handle": "sudipto.me",
                "avatar": "https://cdn-userpic.codeforces.com/306652/avatar/89c71c21b87aa9f8.jpg",
                "firstName": "Sudipto",
                "contribution": 0,
                "organization": "Patuakhali Science and Technology University",
                "rank": "pupil",
                "maxRating": 1420,
                "registrationTimeSeconds": 1432935505,
                "maxRank": "specialist"
            }
            return user_info

        def fake_get_user_sub():
            user_submission = [
                {"verdict": "OK"},
                {"verdict": "TIME_LIMIT_EXCEEDED"},
                {"verdict": "WRONG_ANSWER"},
                {"verdict": "OK"},
                {"verdict": "OK"},
            ]
            return user_submission

        def fake_rating_changes():
            rating_changes = [
                {"contestId": 669},
                {"contestId": 611},
                {"contestId": 700},
            ]
            return rating_changes

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

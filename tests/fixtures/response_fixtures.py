import pytest


@pytest.fixture
def user_info():
    """Returns sample codeforces user.info API response."""
    return {
        "lastName": "Khodyrev",
        "lastOnlineTimeSeconds": 1655498450,
        "rating": 1709,
        "friendOfCount": 92,
        "titlePhoto": "https://cdn-userpic.codeforces.com/1592/title/27e43714e4bea090.jpg",
        "handle": "DmitriyH",
        "avatar": "https://cdn-userpic.codeforces.com/1592/avatar/7cef566902732053.jpg",
        "firstName": "Dmitriy",
        "contribution": 1,
        "organization": "",
        "rank": "expert",
        "maxRating": 2072,
        "registrationTimeSeconds": 1268570311,
        "maxRank": "candidate master"
    }


@pytest.fixture
def user_submission():
    """Sample response of codeforces submission API."""
    return [
        {
            "id": 157298399,
            "contestId": 1677,
            "creationTimeSeconds": 1652613839,
            "relativeTimeSeconds": 2147483647,
            "problem": {
                "contestId": 1677,
                "index": "A",
                "name": "Tokitsukaze and Strange Inequality",
                "type": "PROGRAMMING",
                "points": 500,
                "rating": 1600,
                "tags": [
                    "brute force",
                    "data structures",
                    "dp"
                ]
            },
            "author": {
                "contestId": 1677,
                "members": [
                    {
                        "handle": "Fefer_Ivan"
                    }
                ],
                "participantType": "PRACTICE",
                "ghost": False,
                "startTimeSeconds": 1652020500
            },
            "programmingLanguage": "GNU C++17",
            "verdict": "OK",
            "testset": "TESTS",
            "passedTestCount": 68,
            "timeConsumedMillis": 171,
            "memoryConsumedBytes": 202240000
        }
    ]


@pytest.fixture
def rating_changes():
    """Sample response of user rating API."""
    return [
        {
            "contestId": 1,
            "contestName": "Codeforces Beta Round #1",
            "handle": "Fefer_Ivan",
            "rank": 30,
            "ratingUpdateTimeSeconds": 1266588000,
            "oldRating": 0,
            "newRating": 1502
        },
        {
            "contestId": 2,
            "contestName": "Codeforces Beta Round #2",
            "handle": "Fefer_Ivan",
            "rank": 46,
            "ratingUpdateTimeSeconds": 1267124400,
            "oldRating": 1502,
            "newRating": 1521
        },
        {
            "contestId": 3,
            "contestName": "Codeforces Beta Round #3",
            "handle": "Fefer_Ivan",
            "rank": 77,
            "ratingUpdateTimeSeconds": 1267970400,
            "oldRating": 1521,
            "newRating": 1577
        },
    ]

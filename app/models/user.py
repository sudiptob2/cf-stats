from datetime import datetime

import dateutil.relativedelta

from app.utils.string_utils import Acronym, StringSlicer


class User:
    """Singleton user model."""
    name: str = ''
    organization: str = ''
    rating: int = 0
    rank: str = 'newbie'
    max_rating: int = 0
    max_rank: str = 'newbie'
    contests: int = 0
    submissions: int = 0
    accepted: int = 0
    wrong_ans: int = 0
    tle: int = 0
    contributions: int = 0
    registration_unix_time: int = 0

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(User, cls).__new__(cls)
        return cls.instance

    @classmethod
    def __get_color(cls, rating):
        """Returns the HEX of appropriate color according to the rating."""
        if rating <= 1199:
            col = '#cec8c1'
        elif 1199 < rating <= 1399:
            col = '#43A217'
        elif 1399 < rating <= 1599:
            col = "#22C4AE"
        elif 1599 < rating <= 1899:
            col = "#1427B2"
        elif 1899 < rating <= 2099:
            col = "#700CB0"
        elif 2099 < rating <= 2299:
            col = "#F9A908"
        elif 2299 < rating <= 2399:
            col = "#FBB948"
        else:
            col = "#FF0000"
        return col

    @property
    def rating_color(self):
        return self.__get_color(self.rating)

    @property
    def max_rating_color(self):
        return self.__get_color(self.max_rating)

    @property
    def member_since(self):
        """Returns the number of years at codeforces."""
        joined_at = datetime.fromtimestamp(self.registration_unix_time)
        rd = dateutil.relativedelta.relativedelta(datetime.now(), joined_at)
        return int(rd.years)

    @property
    def org_acronym(self):
        """Provides acronym of the organization."""
        acronym_handler = Acronym()
        return acronym_handler.acronymize(self.organization)

    @property
    def sliced_name(self):
        """Provides a sliced name if the full name is too long."""
        string_handler = StringSlicer()
        return string_handler.slice(self.name)

    def __str__(self):
        """Returns the string rep of the class."""

        return f"Name: {self.name}\nOrg: {self.org_acronym}\nRating: {self.rating}\n" + \
               f"Rank: {self.rank}\nMax Rating: {self.max_rating}\nMax Rank: {self.max_rank}\n" + \
               f"Contests: {self.contests}\nSubmissions: {self.submissions}\nAC: {self.accepted}\n" + \
               f"WA: {self.wrong_ans}\nTLE: {self.tle}\nContribution: {self.contributions}\nSince: {self.member_since}"

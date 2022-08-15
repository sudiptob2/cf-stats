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

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(User, cls).__new__(cls)
        return cls.instance

    def __str__(self):
        """Returns the string rep of the class."""

        return f"Name: {self.name}\nOrg: {self.organization}\nRating: {self.rating}\n" + \
               f"Rank: {self.rank}\nMax Rating: {self.max_rating}\nMax Rank: {self.max_rank}\n" + \
               f"Contests: {self.contests}\nSubmissions: {self.submissions}\nAC: {self.accepted}\n" + \
               f"WA: {self.wrong_ans}\nTLE: {self.tle}\nContribution: {self.contributions}\n"

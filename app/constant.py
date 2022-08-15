from config.config import settings


class Constant:
    """Class for organizing constants."""

    # website names
    CODEFORCES = 'codeforces'
    LOGO = f'{settings.base_dir}/assets/cflogo.svg'

    # API endpoints
    USER_INFO = 'https://codeforces.com/api/user.info?handles={0}'
    USER_STATUS = 'https://codeforces.com/api/user.status?handle={0}'
    USER_RATING = 'https://codeforces.com/api/user.rating?handle={0}'

    # SVG types
    RATING_BADGE = 'rating_badge'
    MAX_RATING_BADGE = 'rating_badge'
    STAT = 'rating_badge'

    # Output folder location
    OUTPUT_FOLDER = f'{settings.base_dir}/output'

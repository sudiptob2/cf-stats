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
    BADGE = 'badge'
    STAT = 'stat'

    # Badge type
    RATING = 'rating'
    MAX_RATING = 'max_rating'

    # Output folder location
    OUTPUT_FOLDER = f'{settings.base_dir}/output'

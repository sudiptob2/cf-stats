from config.config import settings


class Constant:
    """Class for organizing constants."""

    # website names
    CODEFORCES = 'codeforces'
    LOGO = 'https://raw.githubusercontent.com/sudiptob2/cf-stats/main/assets/cflogo.svg'

    # API endpoints
    USER_INFO = 'https://codeforces.com/api/user.info?handles={0}'
    USER_STATUS = 'https://codeforces.com/api/user.status?handle={0}'
    USER_RATING = 'https://codeforces.com/api/user.rating?handle={0}'

    # SVG types
    BADGE = 'badge'
    CARD = 'card'

    # Badge type
    RATING = 'rating'
    MAX_RATING = 'max_rating'
    LIGHT_CARD = 'light_card'

    # Template location
    TEMPLATE_FOLDER = f'{settings.base_dir}/template'

    # Output folder location
    OUTPUT_FOLDER = f'{settings.base_dir}/output'

    # Acronym MAX lenght
    ACC_MAX_LEN = 6

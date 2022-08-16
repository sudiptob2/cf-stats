from app.constant import Constant
from app.services.cf_response_parser import CFResponseParser
from app.services.svg_factory import SVGFactory
from app.utils.file_utils import Config


def main() -> None:
    """This method is used for testing purpose."""
    print('codeforces stat is coming...')
    CFResponseParser.parse()
    generator = SVGFactory.get_svg_generator(Constant.BADGE)

    config = Config(Constant.RATING)
    generator.generate(config)

    config = Config(Constant.MAX_RATING)
    generator.generate(config)
    print('Images are generated in the output folder.')


if __name__ == '__main__':
    main()

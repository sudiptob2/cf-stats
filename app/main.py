from app.constant import Constant
from app.services.cf_response_parser import CFResponseParser
from app.services.svg_factory import SVGFactory
from app.utils.file_utils import Config


def main() -> None:
    """This method is used for testing purpose."""
    print('generating stats...')
    CFResponseParser.parse()

    generator = SVGFactory.get_svg_generator(Constant.BADGE)

    print('generating badges...')
    config = Config(Constant.RATING)
    generator.generate(config)

    config = Config(Constant.MAX_RATING)
    generator.generate(config)
    print('badge generation complete.')

    print('generating stat card...')
    generator = SVGFactory.get_svg_generator(Constant.CARD)
    config = Config(Constant.LIGHT_CARD)
    generator.generate(config)
    print('card generation complete.')
    print('output images are saved in the output folder.')


if __name__ == '__main__':
    main()

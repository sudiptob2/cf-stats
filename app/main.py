from app.services.cf_response_parser import CFResponseParser
from app.services.svg_factory import SVGFactory


def main() -> None:
    """This method is used for testing purpose."""
    print('codeforces stat is coming...')
    CFResponseParser.parse()
    generator = SVGFactory.get_svg_generator('rating_badge')
    generator.generate()


if __name__ == '__main__':
    main()

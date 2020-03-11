import argparse

from atbash import core


def main():
    parser = _build_parser()
    args = parser.parse_args()
    if args.text:
        output = core.cipher(args.text)
        print(output)
    else:
        parser.print_help()


def _build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    return parser

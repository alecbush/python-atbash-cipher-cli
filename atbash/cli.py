import argparse

from . import cipher


def run_command_line():
    parser = _build_parser()
    args = parser.parse_args()
    if args.text:
        output = cipher.cipher_text(args.text)
        print(output)
    else:
        parser.print_help()


def _build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    return parser

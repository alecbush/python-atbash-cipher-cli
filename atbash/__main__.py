import argparse

from .cipher import cipher_text


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    return parser


def run_command_line():
    parser = get_parser()
    args = parser.parse_args()
    if args.text:
        output = cipher_text(args.text)
        print(output)
    else:
        parser.print_help()


if __name__ == "__main__":
    run_command_line()

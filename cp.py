import argparse

def cli():
    parser = argparse.ArgumentParser(
        prog='cp',
        description='Copy files from source to destination.',
        )

    parser.add_argument(
        'source',
        help='Source of the file.'
        )
    parser.add_argument(
        'destination',
        help='Destination to copy the file.'
        )

    args = parser.parse_args()

if __name__ == '__main__':
    cli()
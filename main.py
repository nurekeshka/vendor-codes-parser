from service import Generator
import sys


def main():
    try:
        generator = Generator(sys.argv[1])
    except IndexError as exception:
        raise ValueError('Import filename was not provided in system args.') from exception
    try:
        generator.export(sys.argv[2])
    except IndexError as exception:
        raise ValueError('Export filename was not provided in system args.') from exception


if __name__ == '__main__':
    main()

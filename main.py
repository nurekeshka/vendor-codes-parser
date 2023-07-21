from serializers import Serializer
from generator import Generator
from excel import Excel
import sys


def main():
    try:
        excel = Excel(sys.argv[1])
    except IndexError as exception:
        raise ValueError('Import filename was not provided in system args.') from exception

    serializer = Serializer(excel.rows)
    generator = Generator(serializer.data)

    try:
        generator.export(sys.argv[2])
    except IndexError as exception:
        raise ValueError('Export filename was not provided in system args.') from exception


if __name__ == '__main__':
    main()

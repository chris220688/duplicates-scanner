# Standard library imports
import sys

# Local imports
from duplicatesScanner.duplicates_scanner import DuplicatesScanner


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('usage: bin/duplicatesScanner <directory>')
        sys.exit(0)

    scanner = DuplicatesScanner(sys.argv[1])

    for duplicates in scanner.get_duplicates():
        print(duplicates)
        print('------')
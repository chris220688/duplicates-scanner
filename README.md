# Duplicates Scanner

This is a package that provides functionality to scan a directory tree and identify files with identical content.

The comparisson is done using MD5 checksums, thus the filenames are not taken under consideration.

### Requirements

You need Python 2.7 and above to run the script

You need Python 3.4 and above to run the unit tests

### Usage

Clone the GIT repository in your local machine.

Navigate to the root directory of the project (duplicates-scanner/) and run the executable as:

```
bin/duplicatesScanner <directory>
```

Alternatively, run main.py directly as:

```
python main.py <directory>
```

### Running the tests

We use the pathlib library to create files temporarily, thus Python 3.4 and above is necessary.

To run the unit tests, navigate to the root directory of the project (duplicates-scanner/) and run:

```
python3 -m unittest duplicatesScanner/test/test_duplicates_scanner.py
```

### Authors

Chris Liontos
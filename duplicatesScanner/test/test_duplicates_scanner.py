# Standard library imports
from pathlib import Path
import shutil
import unittest

# Local imports
from duplicatesScanner.duplicates_scanner import DuplicatesScanner


class TestDuplicatesScanner(unittest.TestCase):

    def setUp(self):
        """ Create a temporary file system as:

            root/
            |-- dirA/
            |   |-- file2.txt
            |   |-- sub_dirA/
            |       |-- file5.txt  <-- Duplicate
            |       |-- file6.txt
            |
            |-- dirB/
            |   |-- file3.txt  <-- Duplicate
            |   |-- file4.txt
            |
            |-- file1.txt  <-- Duplicate

        """

        # Create the directories and the files
        self.root_dir = '/tmp/test_dir/'
        self.dirA = self.root_dir + 'dirA/'
        self.dirB = self.root_dir + 'dirB/'
        self.sub_dirA = self.dirA + 'sub_dirA/'

        self.file1 = self.root_dir + 'file1'
        self.file2 = self.dirA + 'file2'
        self.file3 = self.dirB + 'file3'
        self.file4 = self.dirB + 'file4'
        self.file5 = self.sub_dirA + 'file5'
        self.file6 = self.sub_dirA + 'file6'

        Path(self.root_dir).mkdir()
        Path(self.dirA).mkdir()
        Path(self.dirB).mkdir()
        Path(self.sub_dirA).mkdir()

        Path(self.file1).touch()
        Path(self.file2).touch()
        Path(self.file3).touch()
        Path(self.file4).touch()
        Path(self.file5).touch()
        Path(self.file6).touch()

        # Write some content in the files
        with open(self.file1, "w") as file:
            file.write('Duplicate file')

        with open(self.file2, "w") as file:
            file.write('Another duplicate file')

        with open(self.file3, "w") as file:
            file.write('Duplicate file')

        with open(self.file4, "w") as file:
            file.write('This is unique file')

        with open(self.file5, "w") as file:
            file.write('Duplicate file')

        with open(self.file6, "w") as file:
            file.write('Another duplicate file')

        self.scanner = DuplicatesScanner(self.root_dir)

    def tearDown(self):
        # Remove the directory tree, as it is no longer needed
        shutil.rmtree(self.root_dir)

    def test_get_hash(self):

        # It is enough to test one file
        expected_result = '32811caa8cb52b68ed1250e128f3a21e'

        result = self.scanner._get_hash(self.file1)

        self.assertEqual(result, expected_result)

    def test_group_by_hash(self):

        expected_result = {
            '32811caa8cb52b68ed1250e128f3a21e': ['/tmp/test_dir/file1',
                                                 '/tmp/test_dir/dirB/file3',
                                                 '/tmp/test_dir/dirA/sub_dirA/file5'
                                                 ],
            '5623fdd91b0a7a9105f362d615ddff5f': ['/tmp/test_dir/dirA/file2',
                                                 '/tmp/test_dir/dirA/sub_dirA/file6'
                                                 ],
            '953aab4596f63301f8e4fba430cd6fe6': ['/tmp/test_dir/dirB/file4']
        }

        result = self.scanner._group_by_hash()

        self.assertDictEqual(expected_result, result)

    def test_get_files(self):

        expected_result = [
            self.file1, self.file2, self.file3,
            self.file4, self.file5, self.file6
        ]

        result = self.scanner._get_files()

        for res in result:
            self.assertTrue(res in expected_result)

    def test_get_duplicates(self):

        # A list of lists (groups of files) with duplicate content
        expected_result = [
            [self.file1, self.file3, self.file5],
            [self.file2, self.file6]
        ]

        result = self.scanner.get_duplicates()

        for res in result:
            self.assertTrue(res in expected_result)


if __name__ == '__main__':
    unittest.main()

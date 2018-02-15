# Standard library imports
import hashlib
import os


class DuplicatesScanner:
    """ A class that provides functionality to scan
        a directory tree and identify files with
        the same content.
    """

    def __init__(self, directory):
        """ Initialise a DuplicatesScanner instance

            Args:
                directory: The path to the directory to scan
        """

        self.directory = directory

    def _get_hash(self, filename):
        """ Calculate the MD5 checksum of a file.

            Args:
                filename: The file to be hashed

            Returns:
                The MD5 checksum of the file
        """

        chunk_size = 65536
        hasher = hashlib.md5()

        with open(filename, 'rb') as target_file:

            buffer_ = target_file.read(chunk_size)

            while len(buffer_) > 0:
                hasher.update(buffer_)
                buffer_ = target_file.read(chunk_size)

        return hasher.hexdigest()

    def _get_files(self):
        """ Recursively yield all the files from a
            directory tree

            Yields:
                One by one the files under the directory tree
        """

        for root_dir, directories, files in os.walk(self.directory):
            # Ignore hidden files because macOS creates .DS everywhere...
            files = [file for file in files if not file[0] == '.']
            for file in files:
                yield os.path.join(os.path.abspath(root_dir), file)

    def _group_by_hash(self):
        """ Group files by hash

            Returns:
                A dictionary where each key is a hash and each
                value is a list of files that have the same hash
        """

        ordered_by_hash = {}

        for file in self._get_files():
            file_hash = self._get_hash(file)

            if file_hash not in ordered_by_hash:
                ordered_by_hash[file_hash] = [file]
            else:
                ordered_by_hash[file_hash].append(file)

        return ordered_by_hash

    def get_duplicates(self):
        """ Yield lists of files that have the same hashes

            These lists are values from the dict returned
            by _group_by_hash

            Yields:
                Lists that contain more than one files
        """

        grouped_by_hash = self._group_by_hash()

        for key, value in grouped_by_hash.items():
            if len(value) > 1:
                yield value

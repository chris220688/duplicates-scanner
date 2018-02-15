# TODO

### duplicates_scanner.py

*_group_by_hash* is returning a dictionary that has:
* Hashes as keys
* Lists of files as values

Returning a huge dictionary, of storing huge lists in the values of a dictionary might affect the performance.

Need to come up with a better solution to overcome this issue.

### Other

* Investigate whether tempfile libraby is more efficient for creating a temporary directory tree.
* Generate a more user friendly output that might look like a mini report.
* Consider 3rd party libraries (out of the scope of this coding excersise), i.e argparse
* Consider writting the unittests to be backwards compatible with older Python versions.
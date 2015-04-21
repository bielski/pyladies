import unittest
from unittest.mock import *
import os


def remove_file(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)


@patch('remove_tests.os.path')
@patch('remove_tests.os')
class RemoveFileTestCase(unittest.TestCase):

    def test_remove_existing_file(self, mock_os, mock_path):

        # Arrange
        mock_path.isfile.return_value = True
        # Act
        remove_file('any path')
        # Assert
        mock_os.remove.assert_called_with('any path')

    def test_remove_nonexisting_file(self, mock_os, mock_path):

        # Arrange
        mock_path.isfile.return_value = False
        # Act
        remove_file('any path')
        # Assert
        self.assertFalse(mock_os.remove.called, 'Failed to not remove the file if not present.')


# if __name__ == '__main__':
#     unittest.main()

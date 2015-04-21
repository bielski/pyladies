import unittest
import tempfile
import os


def remove_file(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)


class RemoveFileTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), 'tmp-testfile')

    def setUp(self):

        # Arrange
        with open(self.tmpfilepath, 'w') as f:
            f.write('Delete me!')

    def test_remove_file(self):

        # Act
        remove_file(self.tmpfilepath)
        # Assert
        self.assertFalse(os.path.isfile(self.tmpfilepath), 'Failed to remove file!')


# if __name__ == '__main__':
#     unittest.main()

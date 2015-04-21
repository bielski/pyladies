import unittest


class StringTestCase(unittest.TestCase):

    def setUp(self):
        self.name = 'pylady'
        self.nameUpper = 'PYLADY'
        self.nameMixed = 'Pylady'
        self.nameFull = 'Pyladies Poznan'

    def test_upper(self):
        self.assertEqual(self.name.upper(), self.nameUpper)

    def test_is_upper(self):
        self.assertTrue(self.nameUpper.isupper())
        self.assertFalse(self.nameMixed.isupper())

    def test_split(self):
        self.assertEqual(self.nameFull.split(), ['Pyladies', 'Poznan'])

    def test_split_exception(self):
        with self.assertRaises(TypeError):
            self.nameFull.split(2)


# if __name__ == '__main__':
#     unittest.main()




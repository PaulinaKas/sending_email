import unittest
from GIT_emailFV import EditMenu

class EditMenuTest(unittest.TestCase):
    def test_initialization(self):
        editMenuObject = EditMenu()
        self.assertTrue(editMenuObject) # checks if object of class EditMenu exists

    # Given (input sitation)
    # When (some action on this situation)
    # Then (results check)

if __name__ == '__main__':
    unittest.main()

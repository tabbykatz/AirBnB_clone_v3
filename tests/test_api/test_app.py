#!/usr/bin/python3
""" test module for app.py """

import pep8
import unittest


class TestApp(unittest.TestCase):
    """ a class to test app """

    def test_pep8_app(self):
        """ test for pep8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/app.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """ test for docstrings """
        self.assertIsNot(app.__doc__, None,
                         "app.py needs a docstring")
        self.assertTrue(len(app.__doc__) >= 1,
                        "app.py needs a docstring")

#!/usr/bin/python3
""" test module for app.py """

import pep8
import unittest
import pytest
import os
import tempfile
import flask
from api.v1.app import app
from models.engine import db_storage


class appTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    @app_views.route('/status', strict_slashes=False)
    def test_main_page(self):
        response = self.app.get('/status', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


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

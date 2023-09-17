#!/usr/bin/python3
"""Tests for class city """
import unittest
import pep8
from models.city import City


class City_testing(unittest.TestCase):
    """ check class BaseModel """

    def testpep8(self):
        """ testing for codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/city.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

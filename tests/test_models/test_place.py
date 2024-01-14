#!/usr/bin/python3
"""
testing Place
"""
import unittest
import pep8
from models.place import Place

class Place_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pep_stylecode = pep8.StyleGuide(quiet=True)
        path_u = 'models/place.py'
        out_come = pep_stylecode.check_files([path_u])
        self.assertEqual(out_come.total_errors, 0,
                         "Found code style errors (and warnings).")

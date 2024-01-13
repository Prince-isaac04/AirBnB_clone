#!/usr/bin/python3
""" testing city """
import unittest
import pep8
from models.city import City

class City_tested(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pe_pstylecode = pep8.StyleGuide(quiet=True)
        path_u = 'models/city.py'
        re_sult = pe_pstylecode.check_files([path_u])
        self.assertEqual(re_sult.total_errors, 0,
                         "Found code style errors (and warnings).")

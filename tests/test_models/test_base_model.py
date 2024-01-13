#!/usr/bin/python3
""" testing files """
import unittest
import inspect
import pep8
from models.base_model import BaseModel
from datetime import datetime


class BaseModel_testings(unittest.TestCase):
    """ check BaseModel """

    def testspep8(self):
        """ testing codestyle """
        pep_style_codes = pep8.StyleGuide(quiet=True)
        remain = pep_style_codes.check_files(['models/base_model.py',
                                         'models/__init__.py',
                                         'models/engine/file_storage.py'])
        self.assertEqual(remain.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_for_base_modeles(unittest.TestCase):
    """ Class test for BaseModel """
    my_models = BaseModel()

    def TearDownes(self):
        """ delete json file """
        del self.test

    def SetUpes(self):
        """ Create instance """
        self.test = BaseModel()

    def tests_attr_nones(self):
        """None attribute."""
        obj_testes = BaseModel(None)
        self.assertTrue(hasattr(obj_testes, "id"))
        self.assertTrue(hasattr(obj_testes, "created_at"))
        self.assertTrue(hasattr(obj_testes, "updated_at"))

    def tests_kwargs_constructors_2(self):
        """ check id with data """
        dictions = {'score': 100}

        obj_testes = BaseModel(**dictions)
        self.assertTrue(hasattr(obj_testes, 'id'))
        self.assertTrue(hasattr(obj_testes, 'created_at'))
        self.assertTrue(hasattr(obj_testes, 'updated_at'))
        self.assertTrue(hasattr(obj_testes, 'score'))

    def tests_strs(self):
        """ Test string """
        dictions = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        obj_testes = BaseModel(**dictions)
        out = "[{}] ({}) {}\n".format(type(obj_testes).__name__, obj_testes.id, obj_testes.__dict__)

    def tests_to_dicts(self):
        """ check dict """
        obj_testes = BaseModel(score=300)
        n_dictions = obj_testes.to_dict()

        self.assertEqual(n_dictions['id'], obj_testes.id)
        self.assertEqual(n_dictions['score'], 300)
        self.assertEqual(n_dictions['__class__'], 'BaseModel')
        self.assertEqual(n_dictions['created_at'], obj_testes.created_at.isoformat())
        self.assertEqual(n_dictions['updated_at'], obj_testes.updated_at.isoformat())

        self.assertEqual(type(n_dictions['created_at']), str)
        self.assertEqual(type(n_dictions['created_at']), str)

    def tests_datetimes(self):
        """ check datatime """
        bas_ones1 = BaseModel()
        self.assertFalse(datetime.now() == bas_ones1.created_at)

    def tests_BaseModels(self):
        """ check attributes values in a BaseModel """

        self.my_model.name = "Holbie"
        self.my_model.my_number = 100
        self.my_model.save()
        mymodel_jsons = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, mymodel_jsons['name'])
        self.assertEqual(self.my_model.my_number, mymodel_jsons['my_number'])
        self.assertEqual('BaseModel', mymodel_jsons['__class__'])
        self.assertEqual(self.my_model.id, mymodel_jsons['id'])

    def tests_saves_firsts(self):
        """check numbers"""
        with self.assertRaises(AttributeError):
            BaseModel.save([455, 323232, 2323, 2323, 23332])

    def tests_saves_seconds(self):
        """ check string """
        with self.assertRaises(AttributeError):
            BaseModel.save("THIS IS A TEST")

    def test_insts(self):
        """check class """
        let = BaseModel()
        self.assertTrue(let, BaseModel)

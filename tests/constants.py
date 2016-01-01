# -*- coding: utf-8 -*-
import unittest

from ilo_utils.constants import ILO_PORT


class ConstantsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_ilo_port_is_a_number(self):
        self.assertIsInstance(ILO_PORT, int)

    def tearDown(self):
        pass

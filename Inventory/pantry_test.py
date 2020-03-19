#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from datetime import date
from datetime import timedelta
import pantry as p


class PantryTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        pass

    def test_add_item(self):
        user_pantry = p.Pantry()
        text = 'ALFALFA SPROUTS '
        user_pantry.add_item(text)
        self.assertEqual(user_pantry.pantry[text].qty, 1, "item added incorrectly")

    def test_update_qty(self):
        user_pantry = p.Pantry()
        text = 'ALFALFA SPROUTS '
        user_pantry.pantry[text].update_qty(3)
        self.assertEqual(user_pantry.pantry[text].qty, 3, "quantity not updated correctly")

    def test_expiry(self):
        user_pantry = p.Pantry()
        text = 'ALFALFA SPROUTS '
        purchase_date = date.today()
        self.assertEqual(user_pantry.pantry[text].expiration_date, date.today() + timedelta(days = user_pantry.pantry[text].Fridge1) , "expiration date incorrect")

      

# Main: Run Test Cases


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:03:51 2020

@author: audrey.ly
"""

from tab_tuples import *
import unittest

class Test_tab_tuples(unittest.TestCase):
    def test_creation(self):
        tab = tab_tuples()
        self.assertEqual(len(tab.tab), 0)
        tab = tab_tuples([tuple([1,2]), tuple([2,3])])
        self.assertEqual(len(tab.tab), 2)
        self.assertRaises(Exception, tab_tuples, [tuple()])
        self.assertRaises(Exception, tab_tuples, [tuple([1,2]), tuple()])
        
        
    def test_acces_element(self):
        tab = tab_tuples([tuple([1,2])])
        self.assertEqual(tab.getTuple(0),tuple([1,2]))
        self.assertRaises(Exception, tab.getTuple, 1)
        
        
    def test_ajout_element(self):
        tab = tab_tuples()
        tab.ajoute(tuple([1,2]))
        self.assertEqual(len(tab.tab), 1)
        self.assertEqual(tab.getTuple(0),tuple([1,2]))
        self.assertRaises(Exception, tab.ajoute, tuple())
        
        
    def test_supprimer_element(self):
        tab = tab_tuples([tuple([1,2]), tuple([2,3]), tuple([4,5])])
        self.assertRaises(Exception, tab.supprime, 3)
        tab.supprime(1)
        self.assertEqual(len(tab.tab), 2)
        self.assertEqual(tab.getTuple(1),tuple([4,5]))
        tab = tab_tuples()
        self.assertRaises(Exception, tab.supprime,0)


    def test_somme_totale(self):
        tab = tab_tuples([tuple([1,2]), tuple([2,3]), tuple([4,5])])
        res = tab.somme_totale()
        self.assertEqual(res, 17)
        tab = tab_tuples()
        self.assertRaises(Exception, tab.somme_totale)
        
        
    def test_somme_partielle(self):
        tab = tab_tuples([tuple([1,2]), tuple([2,3]), tuple([4,5])])
        res = tab.somme_partielle()
        self.assertEqual(res,[3,5,9])
        tab = tab_tuples()
        self.assertRaises(Exception, tab.somme_partielle)

if __name__ == '__main__':
    unittest.main()
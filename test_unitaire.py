#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:03:51 2020

@author: audrey.ly
"""

from tab_tuples import *
import unittest

class Test_tab_tuples(unittest.TestCase):
    """
        Classe de tests sur les fonctions de la classe tab_tuples
    """
    
    def test_creation(self):
        """
            Tests du constructeur de tab_tuples:
                - constructeur vide
                - constructeur avec un tableau de 2 tuple en paramètre
                - Exception lors de la construction d'un tab_tuples avec des tuples de taille incorrecte (vide, 3 valeurs...)
                - Exception lors de la construction d'un tab_tuples à partir d'un tableau vide
                - Exception lors de la construction d'un tab_tuples à partir d'un tableau de taille > 10
                - Exception lors de la construction d'un tab_tuples à partir d'un tableau de tuple avec une valeur negative
                - Exception lors de la construction d'un tab_tuples à partir d'un tableau contenant un tuple dont la somme des valeurs est > 10
        """
        tab = tab_tuples()
        self.assertEqual(len(tab.tab), 0)
        tab = tab_tuples([tuple([1,2]), tuple([2,8])])
        self.assertEqual(len(tab.tab), 2)
        self.assertRaises(Exception, tab_tuples, [tuple()])
        self.assertRaises(Exception, tab_tuples, [tuple([1,2]), tuple()])
        #test oublié à la création
        self.assertRaises(Exception, tab_tuples,[])
        self.assertRaises(Exception, tab_tuples, [tuple([1,2,3])])
        self.assertRaises(Exception, tab_tuples, [tuple([1])])
        #Nouvelles demandes du client
        self.assertRaises(Exception, tab_tuples,[tuple([1,2]), tuple([1,2]),tuple([1,2]),tuple([1,2]),tuple([1,2]),
                                                 tuple([1,2]),tuple([1,2]),tuple([1,2]),tuple([1,2]),tuple([1,2]),tuple([1,2])])
        self.assertRaises(Exception, tab_tuples, [tuple([0,2]), tuple([-3,1])])
        self.assertRaises(Exception, tab_tuples, [tuple([10,2]), tuple([3,1])])
        
        
    def test_acces_element(self):
        """
            Tests de l'accès aux éléments de tab_tuples (getTuple):
                - Accès correct
                - Accès incorrect : index en dehors du tableau (trop grand, negatif)
                - Acces incorrect : tableau vide
        """
        tab = tab_tuples([tuple([1,2])])
        self.assertEqual(tab.getTuple(0),tuple([1,2]))
        self.assertRaises(Exception, tab.getTuple, 1)
        #tests oubliés à la création
        tab = tab_tuples([tuple([1,2]), tuple([1,2]),tuple([1,2]),tuple([1,2]),tuple([1,2]),
                                                 tuple([1,2]),tuple([3,2]),tuple([1,8])])
        self.assertRaises(Exception, tab.getTuple, -2)
        self.assertRaises(Exception, tab.getTuple, -1)
        tab = tab_tuples()
        self.assertRaises(Exception, tab.getTuple, 0)
        
        
    def test_ajout_element(self):
        """
            Tests de l'ajout d'un élément à un tab_tuples (ajoute):
                - Ajout correct
                - Ajout incorrect d'un tuple de taille incorrect (vide, 1 valeur...)
                - Ajout incorrect d'un tuple comportant un entier negatif
                - Ajout incorrect d'un tuple dont la somme des valeurs est > 10
                - Ajout incorrect d'un tuple à un tableau contenant déjà 10 valeurs
        """
        tab = tab_tuples()
        tab.ajoute(tuple([1,2]))
        self.assertEqual(len(tab.tab), 1)
        self.assertEqual(tab.getTuple(0),tuple([1,2]))
        self.assertRaises(Exception, tab.ajoute, tuple())
        #test oublié à la création
        self.assertRaises(Exception, tab.ajoute, tuple([1,2,3]))
        self.assertRaises(Exception, tab.ajoute, tuple([1]))
        #Nouvelles demandes du client
        self.assertRaises(Exception, tab.ajoute, tuple([-3,1]))
        self.assertRaises(Exception, tab.ajoute, tuple([10,2]))
        tab = tab_tuples([tuple([1,2]), tuple([1,2]),tuple([1,2]),tuple([1,2]),tuple([1,2]),
                                                 tuple([1,2]),tuple([1,2]),tuple([1,2]),tuple([1,2]),tuple([1,2])])
        self.assertRaises(Exception, tab.ajoute,tuple([1,2]))
        
        
    def test_supprimer_element(self):
        """
            Tests de suppression d'un élément à un tab_tuples (supprime):
                - Suppression incorrecte : index en dehors du tableau
                - Suppression correcte
                - Suppression incorrecte sur un tableau vide
                - Suppression incorrecte : index negarif
        """
        tab = tab_tuples([tuple([1,2]), tuple([2,3]), tuple([4,5])])
        self.assertRaises(Exception, tab.supprime, 3)
        tab.supprime(1)
        self.assertEqual(len(tab.tab), 2)
        self.assertEqual(tab.getTuple(1),tuple([4,5]))
        tab = tab_tuples()
        self.assertRaises(Exception, tab.supprime,0)
        #tests oubliés à la création
        tab = tab_tuples([tuple([1,2]), tuple([1,2]),tuple([1,2])])
        self.assertRaises(Exception, tab.supprime, -2)


    def test_somme_totale(self):
        """
            Tests de somme du score d'un tab_tuple :
                - Score sans cas particulier
                - Score incorrect : tableau vide
                - Score avec deux spares
                - Score avec un strike
                - Score avec un spare à la fin
        """
        tab = tab_tuples([tuple([1,2]), tuple([2,3]), tuple([4,5])])
        res = tab.somme_totale()
        self.assertEqual(res, 17)
        tab = tab_tuples()
        self.assertRaises(Exception, tab.somme_totale)
        #Nouvelles demandes du client 2
        tab = tab_tuples([tuple([8,2]), tuple([5,5]), tuple([4,5])])
        self.assertEqual(tab.somme_totale(), 38)
        tab = tab_tuples([tuple([10,0]), tuple([3,5]), tuple([4,5])])
        self.assertEqual(tab.somme_totale(), 35)
        tab = tab_tuples([tuple([0,10]), tuple([5,4]), tuple([5,5])])
        self.assertEqual(tab.somme_totale(), 34)
        
        
    def test_somme_partielle(self):
        """
            Tests de somme partielle du score d'un tab_tuple :
                - Score sans cas particulier
                - Score incorrect : tableau vide
        """
        tab = tab_tuples([tuple([1,2]), tuple([2,3]), tuple([4,5])])
        res = tab.somme_partielle()
        self.assertEqual(res,[3,5,9])
        tab = tab_tuples()
        self.assertRaises(Exception, tab.somme_partielle)
        
    def test_lancer_Jeu(self):
        """
            Tests de lancer_jeu :
                - Strike au round 10 + 2 coups supplémentaires (2 et 5)
                - Strike au round 10 + 2 coups supplémentaires 10 et 10
                - Spare au round 10 + 1 coup supplémentaire de 5
                - Ni spare ni strike au round 10
        """
        valeurs = [3,5,7,3,10,0,0,10,1,1,1,1,2,4,5,1,3,2,10,0,2,5]
        tab = tab_tuples()
        tupleSup, scoretotal = tab.lancer_jeu(valeurs)
        self.assertEqual(scoretotal,99)
        self.assertEqual(tupleSup, tuple([2,5]))
        valeurs = [10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,10]
        tab = tab_tuples()
        tupleSup, scoretotal = tab.lancer_jeu(valeurs)
        self.assertEqual(scoretotal,210)
        self.assertEqual(tupleSup, tuple([10,10]))
        valeurs = [3,5,7,3,2,8,0,10,1,1,1,1,2,4,5,1,3,2,5,5,5]
        tab = tab_tuples()
        tupleSup, scoretotal = tab.lancer_jeu(valeurs)
        self.assertEqual(scoretotal,77)
        self.assertEqual(tupleSup, tuple([5]))
        valeurs = [3,5,7,3,2,8,0,10,1,1,1,1,2,4,5,1,3,2,5,2]
        tab = tab_tuples()
        tupleSup, scoretotal = tab.lancer_jeu(valeurs)
        self.assertEqual(scoretotal,69)
        self.assertEqual(tupleSup, tuple())
        

if __name__ == '__main__':
    unittest.main()
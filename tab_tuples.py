#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:16:24 2020

@author: leila.nedjar
"""

class tab_tuples :

    def __init__(self, tab = None):
        if tab is None:
            self.tab = []
        else :
            for i in range (0, len(tab)):
                if tab[i] is tuple():
                    raise Exception("l'élément : " + str(i) + " est vide !") 
            self.tab = tab
    
    def ajoute(self, element):
        pass
    
    def supprime(self,index):
        if index > len(self.tab)-1:
            raise Exception("Suppression impossible, index out of range !")
        else:
            self.tab.pop(index)
        
    
    def getTuple(self, index):
        if index > len(self.tab)-1:
            raise Exception("Acces element : "+ str(index) +" impossible, index out of range !")
        else:
            return self.tab[index]
    
    def somme_totale(self):
        pass
    
    def somme_partielle(self):
        pass
    
if __name__ == "__main__":
    pass


    
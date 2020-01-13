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
        if element is tuple():
            raise Exception("L'élément que vous essayer d'ajouter est null ")
        self.tab.append(element)
    
    def supprime(self,index):
        pass
    
    def getTuple(self, index):
        pass
    
    def somme_totale(self):
        if len(self.tab) is 0 :
            raise Exception("Le tableau de tuples est vide ")
        res = 0
        for i in range (0,len(self.tab)) :
            res = res + self.tab[i][0] + self.tab[i][1]
        return res
    
    def somme_partielle(self):
        resTab = []
        if len(self.tab) is 0 :
            raise Exception("Le tableau de tuples est vide ")
        for i in range (0,len(self.tab)) :
            resTab.append(self.tab[i][0] + self.tab[i][1])
        return resTab
    
if __name__ == "__main__":
    pass
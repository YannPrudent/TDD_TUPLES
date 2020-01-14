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
            if len(tab) is 0:
                raise Exception("Le tableau est vide")
            if len(tab) > 10:
                raise Exception("Il y a plus de 10 groupes de valeurs dans le tableau")
            for i in range (0, len(tab)):
                if len(tab[i]) is not 2:
                    raise Exception("L'élément : " + str(i) + " a une taille differente de 2")
                if (tab[i][0] + tab[i][1]) > 10:
                    raise Exception("La somme de deux elements du tuple est supérieure a 10")
                if tab[i][0] < 0 or tab[i][1] < 0:
                    raise Exception ("Les entiers d'un tuple ne peuvent être negatifs")    
            self.tab = tab
    
    def ajoute(self, element):
        if len(element) is not 2:
            raise Exception("L'élément que vous essayer d'ajouter est a une taille differente de 2 ")
        if element[0] < 0 or element[1] < 0:
            raise Exception("Les entiers du tuple à ajouter ne peuvent être negatifs")
        if element[0] + element[1] > 10:
            raise Exception("La somme des deux entiers du tuple à ajouter ne peut être supérieure à 10")
        self.tab.append(element)
    
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
        if len(self.tab) is 0 :
            raise Exception("Le tableau de tuples est vide ")
        res = 0
        for i in range (0,len(self.tab)) :
            if (self.tab[i][0] + self.tab[i][1] is 10) and (self.tab[i][0] is not 10) and i+1 < len(self.tab):
                res = res + self.tab[i][0] + self.tab[i][1] + self.tab[i+1][0]
            elif self.tab[i][0] is 10  and i+1 < len(self.tab):
                res = res + self.tab[i][0] + self.tab[i][1] + self.tab[i+1][0] + self.tab[i+1][1]
            else:
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
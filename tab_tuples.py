#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:16:24 2020

@author: leila.nedjar
"""
class tab_tuples :
    """
        Cette classe permet d'avoir un tableau de tuples 
        et les fonctions qui lui sont associées pour travailler avec ce tableau
    """

    def __init__(self, tab = None):
        """
            Cette fonction est le constructeur,
            :param tab: Le constructeur peut être appelé sans paramètres, auquel cas on construit un tableau de tuple vide.
            Si le constructeur est appelé avec un paramètre, qui doit être un tableau de tuple non vide, 
            dans ce cas on recopie le tableau passé en argument dans le tableau de tuples de notre classe.
            :type tab: tableau de tuple.
            
        """
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
        """
            Cette fonction ajoute un élément à notre tableau. 
            :param element: Elle prend en paramètre un élément de deux entiers positifs.
            :type element: tuple.
            Il y a des contraintes à l'ajout d'élément qui sont les suivants : 
                - Les entiers du tuple à ajouter ne peuvent être negatifs.
                - La somme des deux entiers du tuple à ajouter ne peut être supérieure à 10
                - L'élément doit avoir une taille de 2 (tuple de 2 entiers positifs)
        """
        if len(element) is not 2:
            raise Exception("L'élément que vous essayer d'ajouter est a une taille differente de 2 ")
        if element[0] < 0 or element[1] < 0:
            raise Exception("Les entiers du tuple à ajouter ne peuvent être negatifs")
        if element[0] + element[1] > 10:
            raise Exception("La somme des deux entiers du tuple à ajouter ne peut être supérieure à 10")
        self.tab.append(element)
    
    def supprime(self,index):
        """
            Cette fonction supprime un élément du tableau.
            :param index: Elle prend en paramètre un index, correspondant à la case que l'on souhaite supprimer
            :type index: int
            On va venir supprimer l'élément à l'index donné en paramètre.
        """
        if len(self.tab) is 0 :
            raise Exception ("Le tableau est vide")
        if index > len(self.tab)-1 or index < 0:
            raise Exception("Suppression impossible, index out of range !")
        else:
            self.tab.pop(index)
        
    
    def getTuple(self, index):
        """
            Cette fonction renvoie un tuple.
            :param index: Elle prend en paramètre un index correspondant à une case du tableau de tuple.
            :type index: int
            :returns: La fonction renvoie donc le tuple correspondant à l'index donnée.
            :rtype: tuple
        """
        if len(self.tab) is 0 :
            raise Exception ("Le tableau est vide")
        if index > len(self.tab)-1 or index < 0:
            raise Exception("Acces element : "+ str(index) +" impossible, index out of range !")
        else:
            return self.tab[index]
    
    def somme_totale(self):
        """
            Cette fonction effectue la somme totale de chaque éléments de chaque tuple de notre tableau de tuple.
            :returns: La fonction renvoie la somme totale de chaque éléments de chaque tuple de notre tableau de tuple.
            :rtype: int.
        """
        if len(self.tab) is 0 :
            raise Exception("Le tableau de tuples est vide ")
        res = 0
        for i in range (0,len(self.tab)) :
            if (self.tab[i][0] + self.tab[i][1] is 10) and (self.tab[i][0] is not 10) and i+1 < len(self.tab):
                res = res + self.tab[i][0] + self.tab[i][1] + self.tab[i+1][0]
            elif self.tab[i][0] is 10  and i+1 < len(self.tab):
                res = res + self.tab[i][0] + self.tab[i+1][0] + self.tab[i+1][1]
            else:
                res = res + self.tab[i][0] + self.tab[i][1]
        return res
    
    def somme_partielle(self):
        """
            Cette fonction effectue la somme partielle de notre tableau de tuple.
            Elle va aditionner les éléments de chaque tuple un à un et renvoyer un tableau contenant la somme de chaque tuple.
            :returns: tableau contenant la somme de chaque tuple.
            :rtype: tableau de int
        """
        resTab = []
        if len(self.tab) is 0 :
            raise Exception("Le tableau de tuples est vide ")
        for i in range (0,len(self.tab)) :
            resTab.append(self.tab[i][0] + self.tab[i][1])
        return resTab
    
if __name__ == "__main__":
    pass
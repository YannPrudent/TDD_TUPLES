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
            Le tableau passé en argument doit suivre les contraintes suivantes :
                - Le tableau doit contenir des tuples de taille 2 uniquement.
                - Le tuple doit contenir que des entiers.
                - Le tableau passé en argument ne peut pas avoir une taille > 10
                - Les entiers du tuple à ajouter ne peuvent être negatifs.
                - La somme des deux entiers du tuple à ajouter ne peut être supérieure à 10
            :type tab: tableau de tuple (taille <=10)
            
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
                if not isinstance(tab[i][0], int) or not isinstance(tab[i][1], int):
                    raise Exception("Les éléments d'un tuple doivent etre des entiers! ") 
                if (tab[i][0] + tab[i][1]) > 10:
                    raise Exception("La somme de deux elements du tuple est supérieure a 10")
                if tab[i][0] < 0 or tab[i][1] < 0:
                    raise Exception ("Les entiers d'un tuple ne peuvent être negatifs")    
            self.tab = tab
    
    def ajoute(self, element):
        """
            Cette fonction ajoute un élément à notre tableau. 
            :param element: Elle prend en paramètre un élément de deux entiers positifs (tuple).
            :type element: tuple.
            Il y a des contraintes à l'ajout d'élément qui sont les suivants : 
                - On ne peut pas ajouter d'éléments si le tableau a déjà une taille de 10
                - L'élement à ajouter doit contenir deux entiers.
                - Les entiers du tuple à ajouter ne peuvent être negatifs.
                - La somme des deux entiers du tuple à ajouter ne peut être supérieure à 10
                - L'élément doit avoir une taille de 2 (tuple de 2 entiers positifs)
        """
        if len(element) is not 2:
            raise Exception("L'element que vous essayer d'ajouter est a une taille differente de 2 ")
        if not isinstance(element[0], int) or not isinstance(element[1], int) :
            raise Exception("L'élément entré n'est pas un entier! ")
        if element[0] < 0 or element[1] < 0:
            raise Exception("Les entiers du tuple a ajouter ne peuvent etre negatifs")
        if element[0] + element[1] > 10:
            raise Exception("La somme des deux entiers du tuple a ajouter ne peut etre superieure a 10")
        if len(self.tab)+1 > 10: 
            raise Exception("La taille du tableau a depasse 10")
        else :
            self.tab.append(element)
    
    def supprime(self,index):
        """
            Cette fonction supprime un élément du tableau.
            :param index: Elle prend en paramètre un index, correspondant à la case que l'on souhaite supprimer
            :type index: int
            On va venir supprimer l'élément à l'index donné en paramètre.
            Il y a des contraintes pour la suppression d'un élément : 
                - l'index doit être >= 0 
                - l'index doit avoir une taille inférieure à la taille du tableau
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
            Il existe deux cas particuliers correspondant au strike et au spare.
            :returns: La fonction renvoie la somme totale de chaque éléments de chaque tuple de notre tableau de tuple.
            :rtype: int.
        """
        if len(self.tab) is 0 :
            raise Exception("Le tableau de tuples est vide ")
        res = 0
        for i in range (0,len(self.tab)) :
            if (self.tab[i][0] + self.tab[i][1] is 10) and (self.tab[i][0] is not 10) and i+1 < len(self.tab):
                res = res + self.tab[i][0] + self.tab[i][1] + self.tab[i+1][0] #spare
            elif self.tab[i][0] is 10  and i+1 < len(self.tab):
                res = res + self.tab[i][0] + self.tab[i+1][0] + self.tab[i+1][1] #strike
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
    
    def lancer_jeu(self,listValue = None):
        i = 1
        tupleSup = tuple()
        while i <= 10:
            if listValue is None:
                v1 = input("Entrer la premiere valeur de votre "+ str(i) + " tuple \n")
                v2 = input("Entrer la deuxieme valeur de votre "+ str(i) + " tuple \n")
            else :
                v1 = listValue[2*(i-1)]
                v2 = listValue[2*(i-1)+1]
            try :    
                self.ajoute(tuple([v1,v2]))
            except Exception:
                print("La valeur du tuple est incorrect \n")
            else :
                i+=1  
        # spare/ strike         
        if self.tab[-1][0] is 10 :
            while True:
                if listValue is None:
                    v1 = input("Entrer la premiere valeur de votre tuple \n")
                    v2 = input("Entrer la deuxieme valeur de votre tuple \n")
                else :
                    v1 = listValue[20]
                    v2 = listValue[21]
                
                if v1 is 10 and v2 <= 10:
                    tupleSup = tuple([v1,v2])
                    break
                elif v1 + v2 <= 10 and v2 >= 0 and v1 >= 0:
                    tupleSup = tuple([v1,v2])
                    break
                else:
                    print("Valeurs fausses! entrer les valeurs une nouvelle fois")
            score = v1+v2
                
        elif self.tab[-1][0] +self.tab[-1][1] is 10:
            while True:
                if listValue is None:
                    v1 = input("Entrer la premiere valeur de votre tuple \n")
                else :
                    v1 = listValue[20]
                if v1 >= 0 and v1 <= 10 :
                    tupleSup = tuple([v1])
                    break
            score = v1
        else :
            score = 0
        score += self.somme_totale()
        print("Le score est de : " + str(score))
        return tupleSup, score        
                
if __name__ == "__main__":
    
    entree = input("Enter 1 pour lancer le jeu sinon 0\n")
    
    if entree is 1 :
        tab = tab_tuples()
        tab.lancer_jeu()
# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from myparser import *



#Exo 2 Prise en main

#2.1 Creation d’automates

#1
print("--------------------------")

s0 = State(0, True, False)
s1 = State(1, False, False)
s2 = State(2, False, True)

t1 = Transition(s0,"a",s0)
t2 = Transition(s0,"b",s1)
t3 = Transition(s1,"a",s2)
t4 = Transition(s1,"b",s2)
t5 = Transition(s2,"a",s0)
t6 = Transition(s2,"b",s1)

print("Automate A")
auto = Automate([t1,t2,t3,t4,t5,t6])
print(auto)
auto.show("A_ListeTrans")

#2
print("--------------------------")
auto1 = Automate([t1,t2,t3,t4,t5,t6], [s0,s1,s2])
print(auto1)
auto1.show("A_ListeTranscpy")
#l’automateauto1 est bien identique a l’automate auto

#3
automate = Automate.creationAutomate("auto.txt")
print(automate)
automate.show("AutomateFichier")


#2.2 Premieres manipulations

#1
print("--------------------------")
t = Transition(s0,"a",s1)
print(auto.removeTransition(t))
auto.removeTransition(t)
#la transition n'existait pas donc pas de modification
auto.show("A_ListeTrans+remove")

print(auto.addTransition(t))
auto.addTransition(t)
#la transition n'existait pas donc pas on a une transique de l'etat 0 a 1 a
auto.show("A_ListeTrans+add")

#2
print("--------------------------")
auto.removeState(s1)
auto.addState(s1)
s2 = State(0, True, False)
auto.addState(s2)
print(auto)
auto.show("A_ListeTransstate")
#l'etat s1 n'a plus de transition il y'a plus de transition b 

#3
print("--------------------------")
print("les transition de s1 sont")
auto1.getListTransitionsFrom(s1)
print(auto1.getListTransitionsFrom(s1))


#Exercice 3

auto = Automate.creationAutomate("exempleAutomate.txt")
auto.show("exempleAutomate")

#1 
print("--------------------------")
print("les succ sont")
print(auto.succ([s0,s1,s2],'a'))
auto.show("test")


#2
print("--------------------------")
print("accepte")
print(auto.accepte(auto,"abba"))


#3
print("--------------------------")
print("Complet")
print(auto.estComplet(auto,"ab"))

#4
print("--------------------------")
print("estDeterministe")
print(auto.estDeterministe(auto))

#5
print("--------------------------")
print("completeAutomate")
auto.show("Autoc")
print(auto.completeAutomate(auto,"ab"))
auto.completeAutomate(auto,"ab").show("Autoc")

#exo 4 Determinisation
print("--------------------------")
print("Determinisation")
auto.show("Auto")
print(auto.determinisation(auto))
auto.determinisation(auto).show("Autodert")

#exo 5 complementaire
print("complementaire")
auto.show("Auto")
print(auto.complementaire(auto,"ab"))
auto.complementaire(auto,"ab").show("Autocom")
#exo 5 complementaire
print("Intersection")
auto.show("Auto")
print(auto.intersection(auto,auto1))
auto.intersection(auto,auto1).show("AutoInter")
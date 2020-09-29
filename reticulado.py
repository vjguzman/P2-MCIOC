# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:00:50 2020

@author: vjguzman
"""

import numpy as np

class Reticulado(object):
    """Define un reticulado"""

    def __init__(self):
        super(Reticulado, self).__init__()
        
        self.xyz = np.zeros((0,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}

    def agregar_nodo(self, x, y, z=0):
        #Cambiar Tamaño
        self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos +=1
        return
        
    def agregar_barra(self, barra):
        self.barras.append(barra)
        return

    def obtener_coordenada_nodal(self, n): 
        posicion = n
        coordenadas = self.xyz[n]
        return coordenadas

    def calcular_peso_total(self):
        lista_barras = self.barras
        peso_total = 0
        for barra in lista_barras:
            peso_total += barra.calcular_peso(self)
        return peso_total
    
    def obtener_nodos(self):
        xy = self.xyz
        return xy
    
    def obtener_barras(self):
        list_barras = self.barras
        return list_barras

    def agregar_restriccion(self,nodo,gdl, valor=0.0):
        if nodo not in self.restricciones:
            self.restricciones[nodo] = [[gdl,valor]]
        else:
            self.restricciones[nodo].append([gdl,valor])
        return

    def agregar_fuerza(self,nodo,gdl,valor):
        if nodo not in self.cargas:
            self.cargas[nodo] = [[gdl,valor]]
        else:
            self.cargas[nodo].append([gdl,valor])
        return
    def ensamblar_sistema(self):

        return
    def resolver_sistema(self):

        return
    def recuperar_fuerzas(self):

        return

    def __str__(self):
        s = "nodos:\n"
        for n in range(self.Nnodos):
            s+=f'{n} : ( {self.xyz[n,0]}, {self.xyz[n,1]}, {self.xyz[n,2]})\n'
       
        s += "barras:\n"
        for i,b in enumerate(self.barras):
            n = b.obtener_conectividad()
            s+=f'{i} : [{n[0]} {n[1]}]\n'

        s+='restricciones\n'
        for nodo in self.restricciones:
            s+=f'{nodo} : {self.restricciones[nodo]}\n'

        s+='fuerzas\n'
        for nodo in self.cargas:
             s+=f'{nodo} : {self.cargas[nodo]}\n'
        return s

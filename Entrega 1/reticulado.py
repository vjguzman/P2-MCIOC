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


	def __str__(self):
		s = "nodos:\n"
		for i in range(len(self.xyz)):
			s+=f'{i} : ({self.obtener_coordenada_nodal(i)})\n'
		s += "barras:\n"
		for i in range(len(self.barras)):
			s+=f'{i} : {self.barras[i].ni,self.barras[i].nj}\n'
		return s

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:00:50 2020

@author: 56955
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
		coordenadas = self.xyz[n]
		return coordenadas

	def calcular_peso_total(self):
		"""Implementar"""
		return 

	def obtener_nodos(self):
		"""Implementar"""
		peso_total = 0
		for barra in lista_barras:
			peso_total += barra.calcular_peso(self)
		return peso_total

	def obtener_barras(self):
		numero_barra = []
		nodos_barra = []
		for i in range(len(self.barras)):
			nod = []
			numero_barra.append(i)
			nod.append(self.barras[i].ni)
			nod.append(self.barras[i].nj)
			nodos_barra.append(nod)
		return numero_barra,nodos_barra

	def agregar_restriccion(self, nodo, gdl, valor=0.0):
		"""Implementar"""
		return

	def agregar_fuerza(self, nodo, gdl, valor):
		"""Implementar"""
		return

	def ensamblar_sistema(self):
		"""Implementar"""
		return

	def resolver_sistema(self):
		"""Implementar"""
		return

	def recuperar_fuerzas(self):
		"""Implementar"""
		return

	def __str__(self):
		s = "Hola soy un reticulado!\n"
		s += "nodos:\n"
		for i in range(len(self.xyz)):
			s+=f'{i} : ({self.obtener_coordenada_nodal(i)})\n'
		nbarra,nodos = self.obtener_barras()
		s += "barras:\n"
		for i in range(len(self.barras)):
			s+=f'{nbarra[i]} : {nodos[i]}\n'
		return s

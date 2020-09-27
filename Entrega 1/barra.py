# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:58:03 2020

@author: vjguzman
"""

import numpy as np

g = 9.81 #kg*m/s^2


class Barra(object):

	"""Constructor para una barra"""
	def __init__(self, ni, nj, R, t, E, ρ, σy):
		super(Barra, self).__init__()
		self.ni = ni
		self.nj = nj
		self.R = R
		self.t = t
		self.E = E
		self.ρ = ρ
		self.σy = σy

	def obtener_conectividad(self):
		"""Implementar"""
		return 

	def calcular_area(self):
		''' Falta ver unidades de medida'''
		r = self.R - self.t
		area = phi*((self.R**2)-(r**2))
		return area

	def calcular_largo(self, reticulado):
		"""Devuelve el largo de la barra. 
		xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
		xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
		"""
		"""saco las coordenadas (x,y,z) de los nodos"""
		n_i = reticulado.obtener_coordenada_nodal(self.ni)
		n_j = reticulado.obtener_coordenada_nodal(self.nj)


		return 

	def calcular_peso(self, reticulado):
		"""Devuelve el largo de la barra. 
		xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
		xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
		"""
		"""Implementar"""
		a = self.calcular_area()
		largo = self.calcular_largo(reticulado)
		return 
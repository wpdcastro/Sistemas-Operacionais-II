from tabulate import tabulate
from random import randint
import multiprocessing
import os

class Processo : 

	def get_lista_processos(self) :

		processo1 = { 
		    "numero"       : randint(0,9),
		    "burst_time"   : randint(0,9),
		    "hora_chegada" : randint(0,9),
		    "prioridade"   : randint(0,9)
		}

		processo2 = { 
		    "numero"       : randint(0,9),
		    "burst_time"   : randint(20,30),
		    "hora_chegada" : randint(0,9),
		    "prioridade"   : randint(0,9)
		}

		processo3 = { 
		    "numero"       : randint(0,9),
		    "burst_time"   : randint(9,19),
		    "hora_chegada" : randint(0,9),
		    "prioridade"   : randint(0,9)
		}

		fila = [processo1, processo2, processo3]

		return fila
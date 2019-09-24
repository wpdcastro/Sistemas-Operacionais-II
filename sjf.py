from tabulate import tabulate
from random import randint
import multiprocessing
import os
from Processo import Processo 


processo = Processo()
#p.start()

fila = processo.get_lista_processos()

fila_de_prontos = []; 

for fil in fila : 
    
    if (len(fila_de_prontos) == 0) :
        fila_de_prontos.append(fil)
    else :
        if  fila_de_prontos[-1]['burst_time'] < fil['burst_time'] :
            fila_de_prontos.append(fil)
        else :
            aux = fila_de_prontos[-1]
            fila_de_prontos[-1] = fil
            fila_de_prontos.append(aux)

resultados = []

for fifo in fila_de_prontos :
    processo = [fifo['numero'], fifo['burst_time'], fifo['hora_chegada'], "ben10"]
    resultados.append(processo)

tabela = ["Numero" , "Burst Time", "Hora de Chegada", "Tempo de Espera"]

print(tabulate(resultados,tabela,tablefmt="grid"))
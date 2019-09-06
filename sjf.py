from tabulate import tabulate
from random import randint
import multiprocessing
import os

def extrai_info_processo(processo) :

    rg = { 
       "numero"       : os.getegid(),
       "burst_time"   : 27,
       "hora_chegada" : 1
      }

    return rg

def cria_processos() :

    processos = []

    for i in range(3):
        novo_processo = multiprocessing.Process(target=extrai_info_processo)
        processos.append(novo_processo)

    return processos

#processos = cria_processos()
#p.start()

processo1 = { 
    "numero"       : randint(0,9),
    "burst_time"   : randint(0,9),
    "hora_chegada" : randint(0,9)
}

processo2 = { 
    "numero"       : randint(0,9),
    "burst_time"   : randint(0,9),
    "hora_chegada" : randint(0,9)
}

processo3 = { 
    "numero"       : randint(0,9),
    "burst_time"   : randint(0,9),
    "hora_chegada" : randint(0,9)
}

fila = [processo1, processo2, processo3]

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
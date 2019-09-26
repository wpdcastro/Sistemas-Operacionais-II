from tabulate import tabulate
from Processo import Processo
import multiprocessing
import os

processo = Processo()

fila = processo.get_lista_processos()

resultados = []

#print (fila[1]['burst_time'])

print("------------> PROCESSOS <------------")
for process in fila:
    print (process)
    resultados.append(process['burst_time'])
print("\n")

print("------------> Burst Times <------------")
print (resultados)
print("\n\n")

while (len(resultados) > 0) :
    cont = 0
    for processo in resultados :
        quantum = 5

        quanta = fila[cont]['burst_time'] - quantum
        print('Quanta que faltou/sobrou da execução do processo .:.', quanta)

        if (quanta <= 0) :
            fila[0]['burst_time'] = quanta
            resultados.pop(cont)
            print("BURST CONCLUÍDO : PROCESSO ", fila[0]['numero'])
            fila.pop(cont)            
            print("Pendentes -> ", resultados)

        else :
            fila[cont]['burst_time'] = quanta
            cont = cont + 1
            print("Contador ", cont)
            for processo in fila :
                print("PROCESSO ", processo['numero'],"FALTA ", processo['burst_time'])
        
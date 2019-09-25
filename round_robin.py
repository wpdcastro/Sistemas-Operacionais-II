from tabulate import tabulate
from Processo import Processo

processo = Processo()

fila = processo.get_lista_processos()

resultados = []

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
        print('quanta', quanta)

        if (quanta <= 0) :
            fila[0]['burst_time'] = quanta
            resultados.pop(cont)
            fila.pop(cont)
            print("BURST CONCLUÍDO : PROCESSO ", fila[0]['numero'])
            print("Pendentes -> ", resultados)

        else :
            fila[cont]['burst_time'] = quanta
            cont = cont + 1
            print("PROCESSO ", fila[0]['numero'] , "FALTA ", fila[0]['burst_time'])
            print("PROCESSO ", fila[1]['numero'] , "FALTA ", fila[1]['burst_time'])
            print("PROCESSO ", fila[2]['numero'] , "FALTA ", fila[2]['burst_time'])
            print("Contador ", cont)
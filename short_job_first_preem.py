from tabulate import tabulate
from Processo import Processo

processo = Processo()
fila = processo.get_lista_processos()

fila_job = []

for processo in fila :
    print(processo) 

    if (len(fila_job) == 0) :
        fila_job.append(processo)
    else :

        tamanho_processo = processo['burst_time']

        for job in fila_job :
            tamanho_fila     = job['burst_time']
            prioridade_fila  = job['prioridade']

            index = fila_job.index(job)

            if (tamanho_fila < tamanho_processo) :
                index += 1
                fila_job.insert(index, processo)
                break
            else :
                fila_job.insert(index, processo)
                break

resultados = []
for job in fila_job :
    resultados.append([job["numero"], job["burst_time"], job["hora_chegada"], job["prioridade"]])


tabela = ["processo", "burst_time", "hora_chegada", "prioridade"]

print(tabulate(resultados,tabela,tablefmt="grid"))

while (len(resultados) > 0) :
    cont = 0
    for processo in resultados : 
        quantum = 5

        quanta = processo[1] - quantum

        if (quanta <= 0) :
            processo[1] = quanta
            resultados.pop(cont)
            print("BURST CONCLUÍDO : PROCESSO ", processo[0])
            print(resultados)

        else :
            processo[1] = quanta
            print("PROCESSO ", processo[0] , "FALTA ", processo[1])
            print("Conador ", cont)
            cont = cont + 1
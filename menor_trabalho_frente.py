from tabulate import tabulate
from Processo import Processo
#primeiro teste curto 
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

to_print = []
for job in fila_job :
    to_print.append([job["numero"], job["burst_time"], job["hora_chegada"], job["prioridade"]])


tabela = ["processo", "burst_time", "hora_chegada", "prioridade"]

print(tabulate(to_print,tabela,tablefmt="grid"))
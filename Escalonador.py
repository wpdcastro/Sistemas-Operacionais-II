from tabulate import tabulate
from Processo import Processo

class Escalonador : 

    def first_come_first_served(self, fila) :

        fila_de_prontos = []; 
        numero_bursts   = 3;
        soma_burst      = 0;

        for processo in fila : 

            soma_burst = soma_burst + processo['burst_time']
            
            processo['tempo_escolha'] = processo['hora_chegada'] - processo['burst_time'] 
            processo['tempo_medio']   = processo['burst_time']
            
            if (len(fila_de_prontos) == 0) :
                processo['hora_chegada'] = 0
                fila_de_prontos.append(processo)
            else :
                if  fila_de_prontos[-1]['hora_chegada'] < processo['hora_chegada'] :
                    fila_de_prontos.append(processo)
                else :
                    aux = fila_de_prontos[-1]
                    fila_de_prontos[-1] = processo
                    fila_de_prontos.append(aux)

        return fila_de_prontos

    def short_job_first(self,processos) :

        fila_job = []

        for processo in processos :

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

        return fila_job


    def short_job_first_preem(self, processos) :

        fila_job = self.short_job_first(processos)

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
                    print("BURST TIME DO PROCESSO ", processo[0], "CONCLUÍDO")

                else :
                    processo[1] = quanta
                    print("EXECUTANDO ==> PROCESSO ", processo[0] , "| BURST TIME RESTANTE ", processo[1])
                    cont = cont + 1
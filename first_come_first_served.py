from tabulate import tabulate
from Processo import Processo

processo = Processo()
fila = processo.get_lista_processos()

fila_de_prontos = []; 
numero_bursts   = 3;
soma_burst      = 0;

for fil in fila : 

    soma_burst = soma_burst + fil['burst_time']
    
    fil['tempo_escolha'] = fil['hora_chegada'] - fil['burst_time'] 
    fil['tempo_medio']   = fil['burst_time']
    
    if (len(fila_de_prontos) == 0) :
        fil['hora_chegada'] = 0
        fila_de_prontos.append(fil)
    else :
        if  fila_de_prontos[-1]['hora_chegada'] < fil['hora_chegada'] :
            fila_de_prontos.append(fil)
        else :
            aux = fila_de_prontos[-1]
            fila_de_prontos[-1] = fil
            fila_de_prontos.append(aux)

resultados = []

for fifo in fila_de_prontos :
    processo = [fifo['numero'], fifo['burst_time'], fifo['hora_chegada'], fifo['tempo_escolha'], fifo['tempo_medio']]
    resultados.append(processo)

tabela = ["Numero" , "Burst Time", "Hora de Chegada", "Tempo Para Ser Escolhido", "Tempo Médio"]

print(tabulate(resultados,tabela,tablefmt="grid"))

print("Tempo Medio: ", round(soma_burst / numero_bursts, 2))
print("Tempo Que demorou para o processo ser escolhido: ")
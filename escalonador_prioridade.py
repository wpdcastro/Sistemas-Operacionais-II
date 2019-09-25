from tabulate import tabulate
from Processo import Processo
from Escalonador import Escalonador

processo = Processo()
escalonador = Escalonador()

fila = processo.get_lista_processos()
fila_de_prontos = []; 

processos = escalonador.short_job_first(fila)
#processos = escalonador.short_job_first_preem(fila)
#processos = escalonador.first_come_first_served(fila)

#to_print = []
#for processo in processos :
# to_print.append([processo["numero"], processo["burst_time"], processo["hora_chegada"], processo["prioridade"]])

#tabela = ["processo", "burst_time", "hora_chegada", "prioridade"]
#print(tabulate(to_print,tabela,tablefmt="grid"))

processos = escalonador.round_robin(fila)

#tabela = ["processo", "burst_time", "hora_chegada", "prioridade"]

#print(tabulate(fila,tabela,tablefmt="grid"))

### Escalonador de Prioridade
# quando algo é mais importante do que outra coisa
# quantas vezes eu uso aquele processo 
# combinar é sempre uma boa opção
# um cara com alta prioriadade pode causar uma grande fila
# pode se criar quantas categorias quiser moree
# varias filas de pronto, separadas por prioridade 
# escolher se vai fazer do maior pro menor ou ao contrário
# prioridade estática == sempre foi assim e sempre vai sempre
# prioridade dinamica == pode se reduzir/aumentar de acordo com criterios
	#- taxa alta de e/s
	#- quanto do quantum foi usado? se só um pedacinho foi usado,  posso diminuir?

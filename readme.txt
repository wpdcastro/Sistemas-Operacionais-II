Bárbara Caroline - 567620
Bruno Costa      - 568805 
William Castro   - 571644

+-----------------+-----------------------+----------+
|Processo         | Arquivo               | Status   |
+-----------------+-----------------------+----------+
|FCFS             | job_mais_curto        | OK       |
|SJF              | menor_trabalho_frente | OK       |
|SJF (preemptivo) |                       | -        |
|RoundRobin       |                       | -        |
|Prioridades      |                       | -        |
+-----------------+-----------------------+----------+

01/10


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
	- taxa alta de e/s
	- quanto do quantum foi usado? se só um pedacinho foi usado,  posso diminuir?

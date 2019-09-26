Bárbara Caroline - 567620
Bruno Costa      - 568805 
William Castro   - 571644

teste

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

### round robin
# para cada processo é atribuido um quantum identico ao final da execução
# escalonador mantem processos prontos
# quando o quantum do processo se esgota ele é alocado no final da fila e assim sucessivamente
	- problema é a determinação do quantum
	[se e pequeno precisa de muitas trocas - sem eficiencia | se é grande o tempo de resposta nao é aceitavel, deixa muito tempo ocioso]

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

--------------------------------------------
para instalar: 
	from tabulate import tabulate --> instale o tabulate <sudo apt-get install tabulate>
	em escalonador_prioridade.py, altere para o método que quer usar
	rode escalonador_prioridade.py

Bárbara Caroline - 567620
Bruno Costa      - 568805 
William Castro   - 571644

+-----------------+-------------------------+----------+
|Processo         | Arquivo                 | Status   |
+-----------------+-------------------------+----------+
|FCFS             | first_come_first_served | OK       |
|SJF              | job_mais_curto          | OK       |
|SJF (preemptivo) | job_mais_curto_preemp   | OK?      |
|RoundRobin       |                         | - BRUNO  |
|Prioridades      |                         | -        |
+-----------------+-------------------------+----------+

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

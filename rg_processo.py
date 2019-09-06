import multiprocessing
import os

def worker():
    """worker function"""
    print("Bloco de Controle |", os.getegid())
    print("Status:           |")
    print("Group:            |", os.getpgrp())
    print("ID:               |" , os.getpid())
    print("Hierarquia        |", )
    print("pai:              |" , os.getppid())
    print("prioridade:       |", os.getpriority(os.PRIO_PROCESS, os.getpid()))
    print('-----------------------')
    return
    
if __name__ == '__main__':
   
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()


    num_processo = 3
    burst_time = 6


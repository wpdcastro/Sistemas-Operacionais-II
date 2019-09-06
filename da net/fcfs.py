bt=[]
#print("Escreva o numero de processos: ")
#n=int(input())
n = 3

#print("Escreva o burst time: \n")
#bt = input().split()
#bt=list(map(int, bt))

bt = [24, 3 ,3]

wt=[]
avgwt=0
tat=[]
avgtat=0
wt.insert(0,0)
tat.insert(0,bt[0])
for i in range(1,len(bt)):
	wt.insert(i,wt[i-1]+bt[i-1])
	tat.insert(i,wt[i]+bt[i])
	avgwt+=wt[i]
	avgtat+=tat[i]

avgwt=float(avgwt)/n
avgtat=float(avgtat)/n

print("\n")

print("Processo\t  Burst Time\t  Tempo de Espera\t  Tempo de Resposta")

for i in range(0,n):
	print(str(i)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
	print("\n")
print("Tempo médio de espera é: "+ str(avgwt))
print("O Tempo Médio de Entrega de Turno é: "+str(avgtat))
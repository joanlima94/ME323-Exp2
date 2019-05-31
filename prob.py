import random
import matplotlib.pyplot as plt
import os as s

def func_testes(num,vet):
	vet_prob_p = []
	s.system('clear')
	s.system('echo carregando...')
	for j in range(2000):	#número de vezes que vamos testar o problema
		for i in range(num):#funcao que permite gerar números aleatórios com range de 0 até 99,escolhendo 'n1' números
			aleatorio = random.sample(range(0,eleitores),num)
			p.append(vet[aleatorio[i]])
		flag=0
		for k in range(len(p)):
			if p[k] == 1:
				flag+=1
		prob_p = flag/len(p)  
		vet_prob_p.append(round(prob_p,3))
	return vet_prob_p

global testes
global eleitores
testes = 2000
eleitores = 1000
N = []
p = []
vet_prob = []
vet_prob2 = []
tentativas = []

for i in range(testes):
	tentativas.append(i+1)

for i in range(eleitores):	#inicializando vetor N onde há o número total de votos
	if i<(0.3*eleitores):
		N.append(1);
	else:
		N.append(0);

vet_prob = func_testes(5,N)
vet_prob2 = func_testes(100,N)
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (11,7)
plt.plot(tentativas, vet_prob, color = 'green', label = 'Escolhendo 5')
plt.plot(tentativas, vet_prob2, color = 'red', label = 'Escolhendo 100')
plt.legend()
plt.title('Candidatos A e B')
plt.xlabel('Tentativas(N)')
plt.ylabel('Probabilidade(P)')
plt.show()
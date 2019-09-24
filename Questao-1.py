import os

def child():	

	if opcao == 1:
		comando1 = ["/usr/bin/firefox", "www.google.com"]
		os.execve(comando1[0], comando1, os.environ)	

	elif opcao == 2:
		comando2 = ["/usr/bin/gedit"]
		os.execve(comando2[0], comando2, os.environ)
	
	elif opcao == 3:
		comando3 = ["/snap/bin/gnome-calculator"]
		os.execve(comando3[0], comando3, os.environ)
	elif opcao == 4:
		comando4 = ["/usr/bin/nautilus"]
		os.execve(comando4[0], comando4, os.environ)
		

def parent(newpid):
	if (parar == 1):
		pids = (os.getpid(), newpid)
		print("Processo pai: %d, filho: %d \n"%pids)
		ret = os.waitpid(newpid, 0)
		print("Filho terminou com status: ", ret)
	else:
		pids = (os.getpid(), newpid)
		print("Processo pai: %d, filho: %d \n"%pids)

while True:
	
	os.system('clear')
	print("============== ESPERAR/ OU NÃO ESPERAR =================")
	print("0 --> Não Esperar")
	print("1 --> Esperar")
	print("========================================================")
	
	parar = int(input("Digite sua escolha: "))                     
	
	os.system('clear')
	print("------------------------------ MY SHELL -----------------------------")
	print("|			1 - firefox				|")
	print("|			2 - gedit				|")
	print("|			3 - gnome-calculator			|")
	print("|			4 - nautilus				|")
	print("-------------------------------------------------------------------\n")


	opcao = int(input("Digite o que você quer que abra: "))

	


	newpid = os.fork()
	if newpid == 0:
		child()
	
	else:
		parent(newpid)

	reply = input("s para sair / c para um novo trabalho: ")
	if reply == 'c' or reply == 'C':
		continue
	else:
		break

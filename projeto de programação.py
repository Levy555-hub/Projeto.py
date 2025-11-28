def mostrar_menu():
	print("1- transferêcia de anos pra dias")
	print("2- transferêcia de dias pra anos")
	print("3- piada Ruim")
	print("4- sair")

def transferecia_de_anos_pra_dias():
   anos = int(input("numero de anos:"))
   dias = anos * 365
   print(f"o numero de dias {dias} são iguais ao numero de anos {anos}")
   
def transferecia_de_dias_pra_anos():
 	dias = int(input("Numero de Dias:"))
 	anos = dias // 365
 	print(f"O numero de anos {anos} é igual ao numero de dias {dias}")

def piada_Ruim():
	print("Por que o livro de matemática se suicidou?  Porque ele tinha muitos problemas.")
 
while True:
	mostrar_menu()
	opc = input("Qual opção você deseja ?:")	
	
	if opc == "1":
		transferecia_de_anos_pra_dias()
	
	elif  opc  ==  "2":
		transferecia_de_dias_pra_anos()	
	
	elif opc  == "3":
		piada_Ruim()	
	
	elif opc == "4":
		print("saindo...")
		break
	
	else:
		print("opção não encontrada")
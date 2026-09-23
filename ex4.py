import os
os.system('cls')

#Criando a função:
def avaliar_credito(renda: float, score: int) -> tuple[str, float, float]:
    
    #Classificação do cliente:
    if score >= 700:
        cliente = "Cliente VIP"
    elif score >= 500:
        cliente = "Cliente Padrão"
    else:
        cliente = "Cliente Alto Risco"
    
    #Cáculo Do limite aprovado:    
    if cliente == "Cliente VIP":
        limite = renda * 0.80
    elif cliente == "Cliente Padrão":
        limite = renda * 0.40
    else:
        limite = 0
        
    #Taxa de analise:
    if limite > 0:
        taxa = 25.00
    else:
        taxa = 0

    return cliente, limite, taxa

#Solicitando os dados do usuario:
print('--- SOLICITANDO DADOS ---')
renda = float(input('Digite sua renda mensal: '))
score = int(input('Digite seu score: '))

#Chamando a função e Desempacotando ela:
cliente, limite, taxa = avaliar_credito(renda, score)

#Exibindo dados:
print('\n--- EXIBINDO DADOS ---')
print(f'Cliente: {cliente}')
print(f'Limite: R$ {limite:.2f}')
print(f'Taxa: R$ {taxa:.2f}')
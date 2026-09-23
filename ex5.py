import os
os.system('cls')

#Criando a função
def calcular_ingresso(idade: int, tipo_assento: str) -> tuple[str, float, float]:
    
    #Classificar o cliente
    if idade <= 12:
        cliente = "infantil"
    elif idade >= 60:
        cliente = "idoso"
    else:
        cliente = "adulto"
    
    #falar o preço   
    if tipo_assento == "comum":
        preco = 30.00
    else:
        preco = 50.00
    
    #Calcular o desconto
    if cliente == "infantil":
        desconto = preco * 0.50
    elif cliente == "idoso":
        desconto = preco * 0.40
    else:
        desconto = 0.0
        
    valor_final = preco - desconto
    
    #retornando a função
    return cliente, desconto, valor_final

print('--- SOLICITANDO DADOS ---')
idade = int(input('Digite sua idade: '))
tipo_assento = input('Digite seu assento: ').lower()

cliente, desconto, valor_final = calcular_ingresso(idade, tipo_assento)

print('--- EXIBINDO DADOS ---')
print(f'Cliente: {cliente.capitalize()}')
print(f'Desconto: {desconto:.2f}')
print(f'Valor a se pagar: {valor_final:.2f}')
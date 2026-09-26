import os
os.system('cls')

#criando função:
def calcular_fatura_energia(consumo: float, tipo: str) -> tuple[str, float, float, float]:
    #logica do consumo e tipo da fatura:
    if tipo == "R":
        nome_cat = "Residencial"
        if consumo <= 200:
            custo_consumo = consumo * 0.50
        else:
            custo_consumo = consumo * 0.75
    
    else:
        nome_cat = "Comercial"
    if consumo <= 500.00:
        custo_consumo = consumo * 0.60
    else:
        custo_consumo = consumo * 0.90
        
    #taxa iluminação e total:
    taxa_iluminacao = 15.00
    total_fatura = custo_consumo + taxa_iluminacao
    
    #retornando função
    return nome_cat, custo_consumo, taxa_iluminacao, total_fatura

print('--- SOLICITANDO FATURA DE ENERGIA ---')

#loop 1: solicitando consumo
while True:
    try:
        consumo = float(input('O consumo foi de: '))
        if consumo <= 0:
            print('\nDigite um numero de consumo valido(maiores que 0.)')
            continue
        break
    except ValueError:
        print('[ERRO], Digite apenas valores numericos validos\n')
#loop 2: solicitando tipo
while True:
    tipo = input('Tipo de instalação (R - Residencial / C - Comercial): ').strip().upper()
    if tipo in ["R", "C"]:
        break
    else:
        print('[ERRO] Opção inválida! Digite apenas "R" ou "C".\n')

#chamando função e processando:      
nome_cat, custo_consumo, taxa_iluminação, total_fatura = calcular_fatura_energia(consumo, tipo)

#Saida:
print('\n--- EXIBINDO FATURA DE ENERGIA ---')
print(f'Tipo: {nome_cat}')
print(f'custo: R$ {custo_consumo}')
print(f'Taxa de iluminação: R$ {taxa_iluminação}')
print(f'Total da fatura: R$ {total_fatura}')
import os
os.system('cls')

#Criando função
def calcular_envio(peso: float, distancia: float,) -> tuple[str, float, float]:
    
    #Logica do peso
    if peso <= 5.00:
        preco = 15.00
    else:
        preco = 15.00 + ((peso - 5.00) * 4.00)
    
    # Logica da distancia
    if distancia <= 100.00:
        categoria = "Local"
        seguro = 10.00
    else: 
        categoria = "Intermunicipal"
        seguro = 25.00
    
    # Calculando custo total    
    custo_total = preco + seguro
     
    # Retorando a função   
    return categoria, seguro, custo_total

print('--- SOLICITANDO ENVIO ---')

# loop 2: Validação do Peso
while True:
    try:
        peso = float(input('Peso da encomenda: '))
        if peso < 0:
            print('[ERRO], Peso não pode ser menor que 0\n')
            continue
        break
    except ValueError:
            print('[ERRO], Digite apenas valores numericos validos\n')
        
        
    # loop 2: Validação da Distância
while True:
    try:
        distancia = float(input('Distancia percorrida: '))
        if distancia < 0:
            print('[ERRO], Peso não pode ser menor que 0\n')
            continue
        break
    except ValueError:
            print('[ERRO], Digite apenas valores numericos validos\n')
           
# Processamento e saída     
categoria, seguro, custo_total = calcular_envio(peso, distancia)

print('\n--- EXIBINDO DADOS DO ENVIO ---')
print(f'Categoria: {categoria}')
print(f'Custo do seguro: R$ {seguro:.2f}')
print(f'Custo total: R$ {custo_total:.2f}')
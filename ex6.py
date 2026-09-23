import os
os.system('cls')

#Criando a função
def calcular_fatura(dias: int, km: float, categoria: str) -> tuple[str, float, float]:
    if categoria == "economico":
        nome_cat = "ECONOMICO"
        custo_dias = dias * 100.00
    else:
        nome_cat = "SUV"
        custo_dias = 200.00
    
    if km <= 100:
        custo_km = km * 0.50
    else:
        custo_km = km * 0.80
        
        valor_total = custo_km + custo_dias
        
    return nome_cat, custo_km, valor_total

print('--- SOLICITANDO DADOS ---')
modelo = input(('Digite o modelo do carro: '))
km = float(input('Digite os km: '))
dias = int(input('Digite os dias: '))

carro, distancia, total = calcular_fatura(modelo, km, dias)

print('\n--- EXIBINDO DADOS ---')
print(f'O modelo é: {carro}')
print(f'Distancia: {distancia:.2f} KM')
print(f'Dias: {total}')
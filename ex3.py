import os
os.system('cls')

def calcular_frete(distancia: float, peso: float) -> tuple[str, float, float]:
    if distancia > 200:
        status = "Frete Expresso"
    else:
        status = "Frete Padrão"

    if peso > 10:
        adicional_peso = 35.00
    else:
        adicional_peso = 0.00

    valor_total = (distancia * 2.50) + peso
    return status, adicional_peso, valor_total

print('--- SOLICITANDO DADOS ---')

distancia = float(input('Digite a Distancia em Km: '))
peso = float(input('Digite o peso em KG: '))

status_frete, taxa_peso, total_frete = calcular_frete(distancia, peso)

print('\n--- MOSTRANDO DADOS ---')
print(f'Status do frete: {status_frete}')
print(f'Adicional de peso: R$ {taxa_peso:.2f}')
print(f'Total a pagar: R$ {total_frete:.2f}')

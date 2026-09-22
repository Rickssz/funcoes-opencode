import os
os.system('cls')

def calcular_frete(distancia: float, peso: float) -> tuple[str, float, float]:
    peso_adicional = 0
    if peso_adicional > 10:
        frete = 35.00
    else:
        frete = 0

    status_frete = "frete padrão" or "frete expresso"

    valor_total = frete + peso_adicional

    return peso_adicional, frete, valor_total

print('--- SOLICITANDO DADOS ---')

distancia = float(input('Digite a Distancia em Km: '))
peso = float(input('Digite o peso em KG: '))

distancia_final, peso_final, total = calcular_frete(distancia, peso)

print('--- MOSTRANDO DADOS ---')
print(f'A distancia final é: {distancia_final}')
print(f'O peso final é: {peso_final}')
print(f'O total é: {total}')
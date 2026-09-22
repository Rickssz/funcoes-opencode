import os
os.system('cls')

def calcular_salario(salario_base: float, horas_trabalhada: int) -> tuple[float, float, float]:
    valor_hora = salario_base / 160
    hora_extras = max(0, horas_trabalhada - 160)
    
    if hora_extras <= 20:
        extra = hora_extras * valor_hora * 1.5
    else:
        extra = 20 * valor_hora * 1.5 + (hora_extras - 20) * valor_hora * 2
        
    return salario_base + extra, hora_extras, extra
        
print('--- CALCULAR SALARIO ---')
salario = float(input('Digite seu salario: R$ '))
horas = int(input('Digite quantas horas trabalhou: '))

salario_final, qtd_extras, valor_extras, = calcular_salario(salario, horas)

print('\n--- SALARIO CALCULADO ---')
print(f'Horas extras trabalhadas: {qtd_extras}h')
print(f'Valor total das horas extras: R$ {valor_extras:.2f}')
print(f'Seu salario total é: : R$ {salario_final:.2f}')

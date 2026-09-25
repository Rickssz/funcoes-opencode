import os
os.system('cls')

def calcular_salario(salario: float, nivel: int) -> tuple[str, float, float]:
    if nivel == 1:
        categoria = "Excelente"
        bonus = salario * 0.20
    elif nivel == 2:
        categoria = "Bom"
        bonus = salario * 0.10
    elif nivel == 3:
        categoria = "Regular"
        bonus = salario * 0.05
    else:
        categoria = "Sem bónus"
        bonus = 0.0
        
    salario_total = salario + bonus
    
    return categoria, bonus, salario_total

print('--- SOLICITANDO SALARIO ---')

while True:
    try:
        salario = float(input('Seu salario mensal: '))
        if salario < 0:
           print('[ERRO] O salário não pode ser negativo!\n')
           continue 
        nivel = int(input('Seu nivel: '))
        
        categoria, bonus, salario_total = calcular_salario(salario, nivel)
        
        print('\n--- RESUMO DO SALARIO ---')
        print(f'Categoria: {categoria}')
        print(f'Bónus: R$ {bonus:.2f}')
        print(f'Salario_total: R$ {salario_total:.2f}')
        break

    except ValueError:
        print('\n[ERRO] Por favor, digite apenas valores numéricos válidos! ')
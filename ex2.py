import os
os.system('cls')

def calcular_comissao(total_vendas: float) -> tuple[float, float, float]:
    if total_vendas <= 10000.00:
        comissao = total_vendas * 0.05
    else:
        comissao = total_vendas * 0.08
    
    if total_vendas >= 10000.00:
        bonus_fixo = 300.00
    else:
        bonus_fixo = 0.00
    
    total_a_receber = comissao + bonus_fixo
    
    return comissao, bonus_fixo, total_a_receber

print('--- SISTEMA DE COMISSÃO DE VENDAS ---')
vendas = float(input('Digite o valor total de vendas do mês: R$ '))

comissao, bonus, total = calcular_comissao(vendas)

print('\n--- RESUMO DA COMISSÃO ---')
print(f'Comissão: R$ {comissao}')
print(f'Bônus: R$ {bonus}')
print(f'Total a receber: R$ {total}')

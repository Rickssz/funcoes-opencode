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

print('--- ALUGUEL DE VEÍCULOS ---')

try:
    dias = int(input('Quantidade de dias de alugeu: '))
    km = float(input('Quantidade de KM rodados: '))
    categoria = input('Categoria (economico/suv): ').strip().lower()
    
    cat_nome, valor_km, total = calcular_fatura(dias, km, categoria)

    print('\n--- RESUMO DA FATURA ---')
    print(f'Categoria: {cat_nome}')
    print(f'Custo por KM: R$ {valor_km:.2f}')
    print(f'Total a pagar: R$ {total:.2f}')

except ValueError:
    print('\n[ERRO] Por favor, digite apenas valores numéricos válidos!')
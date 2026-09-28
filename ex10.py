import os

def limpar_tela() -> None:
    os.system('cls')
    
def calcular_bilhete(idade: float, tipo: str) -> tuple[str, str, float, float]:
    if idade < 12 or idade > 60:
        entrada = "Meia entrada"
        valor = 15.00
    else:
        entrada = "Entrada Inteira"
        valor = 30.00
        
    if tipo == "D":
        nome_cat = "Dia normal"
        acrescimo = 0.00
    else:
        nome_cat = "Estreia"
        acrescimo = 10.00
        
    valor_total = valor + acrescimo
    
    return entrada, nome_cat, acrescimo, valor_total 

def ler_float(mensagem: str, minimo: float = 0.0) -> float:
    while True:
        try:
            idade = int(input(mensagem))
            if idade <= minimo:
                print(f'[ERRO], A idade deve ser maior que {minimo}!\n')
                continue
            return idade
        except ValueError:
            print('[ERRO] Digite apenas números válidos!\n')
            
def ler_opcao(mensagem: str, opcoes_validas: list[str]) -> str:
    opcoes_formatadas = [op.upper() for op in opcoes_validas]
    while True:
        entrada = input(mensagem).strip().upper()
        if entrada in opcoes_formatadas:
            return entrada
        print(f'[ERRO] Opção inválida! Escolha entre: {", ".join(opcoes_formatadas)}\n')
        
limpar_tela()
print('--- BILHETERIA ---')

idade = ler_float('Digite a sua idade: ', minimo=0.0)
tipo = ler_opcao('O Dia é: ', opcoes_validas=['D', 'E'])

entrada, nome_cat, acrescimo, valor_total = calcular_bilhete(idade, tipo)

print('--- SEU BILHETE ---')
print(f'Sua entrada {entrada}')
print(f'Tipo: {nome_cat}')
print(f'Acréscimo: R$ {acrescimo}')
print(f'Valor total: R$ {valor_total}')
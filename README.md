import os

# --- FUNÇÕES UTILITÁRIAS E AUXILIARES ---
def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_float(mensagem: str, minimo: float = 0.0) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= minimo:
                print(f'[ERRO] O valor deve ser maior que {minimo}!\n')
                continue
            return valor
        except ValueError:
            print('[ERRO] Digite apenas números válidos!\n')

def ler_opcao(mensagem: str, opcoes_validas: list[str]) -> str:
    opcoes_formatadas = [op.upper() for op in opcoes_validas]
    while True:
        entrada = input(mensagem).strip().upper()
        if entrada in opcoes_formatadas:
            return entrada
        print(f'[ERRO] Opção inválida! Escolha entre: {", ".join(opcoes_formatadas)}\n')

# --- REGRA DE NEGÓCIO ---
def calcular_bilhete(idade: float, tipo: str) -> tuple[str, str, float, float]:
    if idade < 12 or idade >= 60:
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


# --- PROGRAMA PRINCIPAL ---
limpar_tela()

# Lista para armazenar o valor de cada bilhete vendido no dia
vendas: list[float] = []

print('====================================')
print('   SISTEMA DE VENDAS - CINEMA       ')
print('====================================')

while True:
    print('\n--- NOVO ATENDIMENTO ---')
    
    # Solicitando dados
    idade = ler_float('Digite a idade do cliente: ', minimo=0.0)
    tipo = ler_opcao('Tipo de sessão (D - Normal / E - Estreia): ', opcoes_validas=['D', 'E'])

    # Processamento
    entrada, nome_cat, acrescimo, valor_total = calcular_bilhete(idade, tipo)

    # Registro do valor
    vendas.append(valor_total)

    # Exibição do recibo do cliente
    print('\n--- RECIBO DO BILHETE ---')
    print(f'Sua entrada: {entrada}')
    print(f'Tipo: {nome_cat}')
    print(f'Acréscimo: R$ {acrescimo:.2f}')
    print(f'Valor total: R$ {valor_total:.2f}')
    print('--------------------------')

    # Pergunta se deseja continuar o atendimento
    continuar = ler_opcao('\nDeseja atender outro cliente? (S/N): ', opcoes_validas=['S', 'N'])
    
    if continuar == 'N':
        break
    
    # Limpa a tela para o próximo cliente
    limpar_tela()

# --- RELATÓRIO DE ENCERRAMENTO ---
limpar_tela()
print('====================================')
print('   RESUMO DO EXPEDIENTE (FECHAMENTO)')
print('====================================')
print(f'Total de bilhetes vendidos: {len(vendas)}')
print(f'Faturamento total do dia:   R$ {sum(vendas):.2f}')
print('====================================\n')
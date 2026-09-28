import os

def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Função Principal
def processar_notas(notas: list[float]) -> tuple[float, str, list[float]]:
    # 1. Calculando a média
    media = sum(notas) / len(notas)
    
    # 2. Definindo o status
    if media >= 7.0:
        status = 'Aprovado'
    elif media >= 5.0:
        status = 'Recuperação'
    else:
        status = 'Reprovado'
        
    # 3. Filtrando notas acima da média
    acima_da_media = []
    for nota in notas:
        if nota > media:
            acima_da_media.append(nota)
        
    return media, status, acima_da_media


# --- PROGRAMA PRINCIPAL ---
limpar_tela()
print('--- PROCESSAMENTO DE NOTAS ---')

notas = []

# Coletando 4 notas e guardando na lista
for i in range(4):
    while True:
        try:
            nota = float(input(f'Digite a {i+1}ª nota (0 a 10): '))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            print('[ERRO] A nota deve estar entre 0 e 10!\n')
        except ValueError:
            print('[ERRO] Digite apenas números válidos!\n')

# Chamando a função
media, status, acima_da_media = processar_notas(notas)

# Exibindo resultados
print('\n--- RESULTADO FINAL ---')
print(f'Notas digitadas: {notas}')
print(f'Média do aluno: {media:.2f}')
print(f'Status: {status}')
print(f'Notas acima da média: {acima_da_media}')
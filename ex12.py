import os

def limpar_tela():
    os.system('cls')
    
def analisar_mensagens(mensagens: list[str]) -> tuple[int, list[str], list[str]]:
    total_palavras = 0
    curtas = []
    urgentes = []
    
    for msg in mensagens:
        palavras = msg.split()
        qtd_palavras = len(palavras)

        
        total_palavras += qtd_palavras
    
        if qtd_palavras < 5:
            curtas.append(msg)
        
        if "urgente" in msg.lower():
            urgentes.append(msg)
        
    return total_palavras, curtas, urgentes

print('--- ANALISADOR DE MENSAGENS ---')

mensagens = []

limpar_tela()
for i in range(4):
    while True:
        texto = input(f'Digite {i+1}° mensagem: ').strip()
        
        if len(texto) > 0:
            mensagens.append(texto)
            break
        
        print('[ERRO] A mensagem não pode ficar em branco!\n')
        
total_palavras, curtas, urgentes = analisar_mensagens(mensagens)

print('\n--- MENSAGENS ANALISADAS ---')
print(f'Total palavras: {total_palavras}')
print(f'Mensagens curtas: {curtas}')
print(f'Urgentes: {urgentes}')

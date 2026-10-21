def adicionar_item(nome, preco, quantidade=1):
    if nome:
        preco += quantidade
    return preco

def remover_item(nome, itens):
    if nome:
        for i, item in enumerate(itens):
            if item['nome'] == nome:
                itens.pop(i)
                return f"{nome} removido do carrinho"
    else:
        raise ValueError("Nome do item não pode ser vazio")
    
def show(itens):
    for item in itens:
        print(f"{item['nome']} - {item['preco']} - {item['quantidade']}")

def calcular_frete(frete, total):
    if total >= 150:
        frete == 0
    else:
        frete == 20
    return frete

def total(Carrinho):
    total = 0
    if Carrinho is None:
        total = 0
    else:
        for item in Carrinho:
            total += item['preco'] * item['quantidade']
    return total

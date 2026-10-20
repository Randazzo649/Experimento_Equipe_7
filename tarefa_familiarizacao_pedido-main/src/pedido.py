def calcular_total_pedido(subtotal, distancia_km, cliente_vip=False):
    """Calcula o valor final de um pedido.

    A implementação inicial contém defeitos e deve ser corrigida
    de acordo com os requisitos descritos no README.
    """

    if subtotal < 0 or distancia_km < 0:
        raise ValueError("Subtotal e distância não podem ser negativos")

    if cliente_vip:
        desconto = subtotal * 0.1
    else:
        desconto = 0

    subtotal_com_desconto = subtotal - desconto


    if subtotal_com_desconto >= 100:
        frete = 0
    else:
        frete = 8 + distancia_km * 1.5

    total = subtotal_com_desconto + frete
    return total 

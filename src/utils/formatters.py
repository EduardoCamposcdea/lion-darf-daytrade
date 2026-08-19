from decimal import Decimal, ROUND_HALF_UP

def formatar_moeda(valor: Decimal) -> str:
    valor_arredondado = valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"R$ {valor_arredondado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
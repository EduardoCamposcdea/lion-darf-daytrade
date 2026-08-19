from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

@dataclass(frozen=True)
class ApuracaoDayTrade:
    lucro_mes: Decimal
    prejuizo_acumulado: Decimal
    irrf_total: Decimal

    ALIQUOTA_DAY_TRADE: Decimal = Decimal("0.20")
    VALOR_MINIMO_DARF: Decimal = Decimal("10.00")

    @property
    def base_calculo(self) -> Decimal:
        return max(Decimal("0.00"), self.lucro_mes - self.prejuizo_acumulado)

    @property
    def imposto_devido(self) -> Decimal:
        bruto = self.base_calculo * self.ALIQUOTA_DAY_TRADE
        return bruto.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @property
    def darf_calculado(self) -> Decimal:
        return max(Decimal("0.00"), self.imposto_devido - self.irrf_total)

    @property
    def darf_a_pagar(self) -> Decimal:
        valor = self.darf_calculado
        return valor if valor >= self.VALOR_MINIMO_DARF else Decimal("0.00")

    @property
    def irrf_excedente(self) -> Decimal:
        if self.irrf_total > self.imposto_devido:
            return self.irrf_total - self.imposto_devido
        return Decimal("0.00")
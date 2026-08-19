from decimal import Decimal
import streamlit as st

from src.models.apuracao import ApuracaoDayTrade
from src.utils.formatters import formatar_moeda
from src.styles.css import CUSTOM_CSS

st.set_page_config(
    page_title="LION DARF – Day Trade",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def inicializar_estado():
    defaults = {"lucro": 0.0, "prejuizo": 0.0, "irrf_total": 0.0}
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def limpar_dados():
    st.session_state.lucro = 0.0
    st.session_state.prejuizo = 0.0
    st.session_state.irrf_total = 0.0

inicializar_estado()

@st.dialog("Como funciona a apuração de Day Trade?")
def exibir_modal_ajuda():
    st.markdown("""
    ### 📘 Guia Prático de Imposto para Traders
    
    **1. A Regra da Receita Federal (20% Fixo)**
    Diferente do Swing Trade, **Day Trade não possui isenção dos R$ 20.000**. Teve lucro líquido acumulado no mês (ganhos menos custos e prejuízos), a alíquota devida é de **20%** sobre a base de cálculo.

    ---

    **2. O que é o IRRF ("Dedo-Duro")?**
    Em todo dia que você fecha no **positivo**, a corretora retém obrigatoriamente **1% sobre o lucro daquele dia** a título de Imposto de Renda Retido na Fonte. Esse valor vai direto para a Receita Federal para avisar que você operou.

    ---

    **3. Como Usar o IRRF de Meses Anteriores (Meses de Prejuízo)**
    Mesmo que o seu mês termine no **prejuízo geral**, você pode ter tido dias vencedores em que o IRRF foi recolhido.
    * **Esse imposto não é perdido!** Ele se transforma em um **crédito fiscal acumulado**.
    * Você pode somar todo o IRRF recolhido nos meses de prejuízo e **descontar do imposto devido** no primeiro mês em que fechar no lucro.

    ---

    **4. A Regra dos R$ 10,00 para Emissão do DARF**
    A Receita Federal **não aceita pagamentos de DARF com valor inferior a R$ 10,00**.
    * Se o imposto calculado no mês for **menor que R$ 10,00** (ex: R$ 8,35), **você não emite DARF este mês**.
    * O valor não é perdoado: ele é somado ao cálculo do próximo mês até atingir ou ultrapassar a trava de R$ 10,00.
    """)
    if st.button("Entendi", use_container_width=True):
        st.rerun()

header_col1, header_col2 = st.columns([2, 1], vertical_alignment="center")

with header_col1:
    st.markdown("""
        <div class="brand-logo">
            <div class="brand-logo-icon">🦁</div>
            <div>
                <div class="brand-title">LION DARF</div>
                <div class="brand-subtitle">INVESTIMENTOS</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with header_col2:
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("❓ Ajuda", use_container_width=True):
            exibir_modal_ajuda()
    with btn_col2:
        if st.button("🔄 Resetar", on_click=limpar_dados, use_container_width=True):
            st.rerun()

with st.container(border=True):
    st.markdown("""
        <div class="card-header-icon">🧮</div>
        <div class="main-title">Apurador <span>Day Trade</span></div>
        <div class="main-subtitle">Calcule o imposto das suas operações e saiba exatamente o valor do seu DARF.</div>
        
        <div class="stepper">
            <div class="step-item active">
                <div class="step-number">1</div>
                <span>Apuração do Mês</span>
            </div>
            <div class="step-line"></div>
            <div class="step-item">
                <div class="step-number">2</div>
                <span>Dedução de IRRF</span>
            </div>
            <div class="step-line"></div>
            <div class="step-item">
                <div class="step-number">3</div>
                <span>Emissão DARF</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    form_col, result_col = st.columns([1, 1], gap="large")

    with form_col:
        st.markdown("##### 📝 Dados da Apuração")
        lucro_in = st.number_input("Lucro Líquido do Mês (R$)", min_value=0.0, step=100.0, key="lucro")
        prejuizo_in = st.number_input("Prejuízo Acumulado Anterior (R$)", min_value=0.0, step=100.0, key="prejuizo")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### 📑 Créditos de Imposto")
        irrf_total_in = st.number_input("Total de IRRF Disponível (Mês + Acumulado) (R$)", min_value=0.0, step=10.0, key="irrf_total")

    apuracao = ApuracaoDayTrade(
        lucro_mes=Decimal(str(lucro_in)),
        prejuizo_acumulado=Decimal(str(prejuizo_in)),
        irrf_total=Decimal(str(irrf_total_in)),
    )

    with result_col:
        st.markdown("##### 📊 Resumo do Cálculo")

        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric("Base de Cálculo", formatar_moeda(apuracao.base_calculo))
            st.metric("Crédito IRRF Usado", formatar_moeda(apuracao.irrf_total))
        with res_col2:
            st.metric("Imposto Devido (20%)", formatar_moeda(apuracao.imposto_devido))

        st.markdown(f"""
            <div class="darf-card-hero">
                <div class="darf-card-label">VALOR DO DARF A PAGAR</div>
                <div class="darf-card-amount">{formatar_moeda(apuracao.darf_a_pagar)}</div>
            </div>
        """, unsafe_allow_html=True)

        if Decimal("0.00") < apuracao.darf_calculado < apuracao.VALOR_MINIMO_DARF:
            st.markdown(f"""
                <div class="carry-over-box">
                    <div>
                        <p class="carry-over-title">📌 Imposto Acumulado p/ Próximo Mês</p>
                        <p class="carry-over-sub">Guarde este valor para somar na próxima apuração</p>
                    </div>
                    <div class="carry-over-value">{formatar_moeda(apuracao.darf_calculado)}</div>
                </div>
            """, unsafe_allow_html=True)
        elif apuracao.irrf_excedente > Decimal("0.00"):
            st.markdown(f"""
                <div class="carry-over-box">
                    <div>
                        <p class="carry-over-title">📌 Crédito de IRRF Restante</p>
                        <p class="carry-over-sub">Sobra de IRRF disponível para abater em meses futuros</p>
                    </div>
                    <div class="carry-over-value">{formatar_moeda(apuracao.irrf_excedente)}</div>
                </div>
            """, unsafe_allow_html=True)

        if Decimal("0.00") < apuracao.darf_calculado < apuracao.VALOR_MINIMO_DARF:
            st.markdown(f"""
                <div class="custom-alert custom-alert-warning">
                    ⚠️ Atenção: O valor apurado ({formatar_moeda(apuracao.darf_calculado)}) é inferior ao mínimo de R$ 10,00. Não emita DARF este mês.
                </div>
            """, unsafe_allow_html=True)
        elif apuracao.darf_a_pagar >= apuracao.VALOR_MINIMO_DARF:
            st.markdown("""
                <div class="custom-alert custom-alert-success">
                    ✅ DARF Gerado! Pague sob o código 6015 até o último dia útil do mês seguinte.
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="custom-alert custom-alert-info">
                    ℹ️ Isento de DARF: Não há imposto a pagar para a apuração deste mês.
                </div>
            """, unsafe_allow_html=True)

    st.markdown("""
        <div class="trust-footer">
            🔒 Suas informações estão protegidas e os cálculos seguem as normas da Receita Federal.
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="features-bar">
        <div class="feature-item">
            <div class="feature-icon">🛡️</div>
            <div>
                <div class="feature-title">Segurança Total</div>
                <div class="feature-desc">Precisão Decimal exata de acordo com a Receita.</div>
            </div>
        </div>
        <div class="feature-item">
            <div class="feature-icon">📈</div>
            <div>
                <div class="feature-title">Day Trade 20%</div>
                <div class="feature-desc">Cálculo de deduções de IRRF e prejuízos.</div>
            </div>
        </div>
        <div class="feature-item">
            <div class="feature-icon">⭐</div>
            <div>
                <div class="feature-title">Regra dos R$ 10</div>
                <div class="feature-desc">Aviso para não pagar DARF mínimo acumulado.</div>
            </div>
        </div>
        <div class="feature-item">
            <div class="feature-icon">⚡</div>
            <div>
                <div class="feature-title">Rápido e Fácil</div>
                <div class="feature-desc">Simule em poucos minutos e evite multas.</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
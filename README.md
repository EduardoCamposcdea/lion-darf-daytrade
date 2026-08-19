# 🦁 LION DARF – Apurador de Imposto em Day Trade

Uma aplicação web moderna, precisa e intuitiva desenvolvida em **Python (Streamlit)** para auxiliar investidores e traders no cálculo exato do Imposto de Renda (IR) e verificação do valor devido para emissão de DARF em operações de Day Trade na Bolsa de Valores (B3).

---

## 🎯 Sobre o Projeto & Visão do Criador

Este projeto foi construído combinando **Domínio de Negócio / UX** com **Desenvolvimento Assistido por Inteligência Artificial (AI-Assisted Development)**. 

Como idealizador do projeto, atuei no papel de **Product Owner e Prompt Engineer**:
* **Definição da Regra de Negócio:** Especificação técnica detalhada das leis fiscais da Receita Federal para renda variável.
* **Orquestração da Arquitetura:** Direcionamento da IA para criar uma estrutura limpa, modular e separada por responsabilidades (`src/models`, `src/styles`, `src/utils`).
* **Design & UX:** Validação e refinamento contínuo da interface visual, paleta de cores SaaS financeira e experiência do usuário.

---

## 🧮 Regras de Negócio e Funcionalidades Suportadas

O sistema aplica automaticamente as diretrizes fiscais brasileiras para operações de Day Trade:

1. **Alíquota Fixa de 20%:** Cálculo automático sobre o lucro líquido (sem isenção mensal dos R$ 20.000, que se aplica apenas a Swing Trade).
2. **Compensação de Prejuízos Anteriores:** Abatimento de prejuízos acumulados em meses passados da base de cálculo atual.
3. **Créditos de IRRF ("Dedo-Duro"):** Abatimento total do Imposto de Renda Retido na Fonte (mês atual + meses anteriores em que houve saldo de IRRF não compensado).
4. **Trava do Valor Mínimo de R$ 10,00 (Receita Federal):** Identificação de DARFs com valor inferior a R$ 10,00. O sistema orienta o usuário a não emitir a guia no mês e acumular o saldo para a próxima apuração.
5. **Precisão Financeira (`Decimal`):** Utilização da biblioteca `Decimal` nativa do Python com arredondamento `ROUND_HALF_UP`, evitando erros de precisão numéricos.

---

## 📁 Arquitetura do Projeto

O código foi organizado seguindo o princípio de **Separação de Responsabilidades (Separation of Concerns)**:

```text
lion-darf-daytrade/
│
├── app.py                     # Orquestrador da Interface Streamlit
├── requirements.txt           # Dependências do Projeto
├── README.md                  # Documentação do Repositório
│
└── src/
    ├── models/
    │   └── apuracao.py        # Classe ApuracaoDayTrade (Regra de Negócio Fiscal)
    ├── styles/
    │   └── css.py             # CSS Customizado (Identidade Visual & Paleta)
    └── utils/
        └── formatters.py      # Formatadores de Moeda e Números (R$)

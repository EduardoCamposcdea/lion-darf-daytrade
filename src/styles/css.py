CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    #MainMenu, header, footer { visibility: hidden; }

    /* Fundo da Aplicação Principal */
    .stApp {
        background: linear-gradient(135deg, #F3F5FC 0%, #EAEFFC 50%, #F5F0FF 100%);
        background-attachment: fixed;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 1100px !important;
    }

    /* Cartão Container Principal */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF !important;
        border-radius: 24px !important;
        padding: 2.5rem !important;
        box-shadow: 0 12px 40px rgba(99, 49, 232, 0.06) !important;
        border: 1px solid rgba(225, 228, 236, 0.6) !important;
    }

    /* Rótulos e textos gerais */
    .stApp p, .stApp span, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4,
    [data-testid="stWidgetLabel"] *, 
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span {
        color: #111A3A;
    }

    /* CARD ROXO DO DARF (Garante fundo roxo e texto 100% branco) */
    .darf-card-hero {
        background: linear-gradient(135deg, #6331E8 0%, #4B1EC6 100%) !important;
        border-radius: 18px !important;
        padding: 1.8rem !important;
        text-align: center !important;
        box-shadow: 0 10px 25px rgba(99, 49, 232, 0.22) !important;
        margin-top: 1rem !important;
    }

    .darf-card-hero,
    .darf-card-hero *,
    [data-testid="stMarkdownContainer"] .darf-card-hero * {
        color: #FFFFFF !important;
    }

    .darf-card-label { font-size: 0.8rem; font-weight: 700; letter-spacing: 1.2px; opacity: 0.9; text-transform: uppercase; }
    .darf-card-amount { font-size: 2.8rem; font-weight: 800; margin: 0.2rem 0; }

    /* Cabeçalho e Marca */
    .brand-logo { display: flex; align-items: center; gap: 12px; margin-bottom: 1rem; }
    .brand-logo-icon { font-size: 2rem; background: #FFFFFF; padding: 6px 12px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .brand-title { font-weight: 800; font-size: 1.25rem; color: #111A3A !important; margin: 0; line-height: 1.1; }
    .brand-subtitle { font-weight: 600; font-size: 0.75rem; color: #6331E8 !important; letter-spacing: 1px; }

    .card-header-icon { width: 52px; height: 52px; background: #F0EBFB; color: #6331E8 !important; border-radius: 14px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; font-size: 1.6rem; }
    .main-title { text-align: center; font-weight: 800; font-size: 2.2rem; color: #111A3A !important; margin-bottom: 0.3rem; }
    .main-title span { color: #6331E8 !important; }
    .main-subtitle { text-align: center; color: #68718B !important; font-size: 0.95rem; margin-bottom: 2rem; }

    /* Barra de Progresso (Stepper) */
    .stepper { display: flex; justify-content: center; align-items: center; gap: 1.2rem; margin-bottom: 2.5rem; background: #FAFAFC; padding: 12px 24px; border-radius: 16px; border: 1px solid #E1E4EC; }
    .step-item { display: flex; align-items: center; gap: 8px; font-size: 0.85rem; font-weight: 600; color: #8C94A8 !important; }
    .step-item.active { color: #111A3A !important; }
    .step-number { width: 26px; height: 26px; border-radius: 50%; background: #E8ECEF; color: #68718B !important; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: 700; }
    .step-item.active .step-number { background: #6331E8; color: #FFFFFF !important; }
    .step-line { width: 30px; height: 2px; background: #E8ECEF; }

    /* Caixas de Informação */
    .carry-over-box { background-color: #F8F9FE; border: 1px dashed #6331E8; border-radius: 14px; padding: 1rem 1.2rem; margin-top: 1rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
    .carry-over-title { font-size: 0.82rem; font-weight: 700; color: #111A3A !important; margin: 0; }
    .carry-over-sub { font-size: 0.73rem; color: #68718B !important; margin: 0; }
    .carry-over-value { font-size: 1.25rem; font-weight: 800; color: #6331E8 !important; white-space: nowrap; flex-shrink: 0; text-align: right; }

    .custom-alert { padding: 0.85rem 1.1rem; border-radius: 12px; font-size: 0.85rem; font-weight: 500; line-height: 1.4; display: flex; align-items: center; gap: 10px; margin-top: 1rem; }
    .custom-alert-warning { background-color: #FFF8E6; color: #8A5300 !important; border: 1px solid #FFE5A3; }
    .custom-alert-success { background-color: #E6F8EF; color: #0D6832 !important; border: 1px solid #B3ECC8; }
    .custom-alert-info { background-color: #EBF3FE; color: #1E40AF !important; border: 1px solid #BFDBFE; }

    .trust-footer { text-align: center; color: #8C94A8 !important; font-size: 0.82rem; margin-top: 2rem; }
    .features-bar { background: #FFFFFF; border-radius: 20px; padding: 1.2rem 1.8rem; margin-top: 2rem; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); border: 1px solid rgba(225, 228, 236, 0.6); display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; }
    .feature-item { display: flex; align-items: center; gap: 12px; }
    .feature-icon { width: 40px; height: 40px; border-radius: 50%; background: #F0EBFB; color: #6331E8 !important; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; }
    .feature-title { font-weight: 700; font-size: 0.85rem; color: #111A3A !important; margin: 0; }
    .feature-desc { font-size: 0.73rem; color: #79829A !important; margin: 0; }

    /* Inputs e Botões (Ajuda / Resetar) */
    div[data-baseweb="input"] { border-radius: 12px !important; border: 1px solid #E1E4EC !important; background-color: #FAFAFC !important; }
    div[data-baseweb="input"] input { color: #111A3A !important; }

    div[data-testid="stButton"] > button {
        background-color: #FFFFFF !important;
        border: 1px solid #E1E4EC !important;
    }
    div[data-testid="stButton"] > button * {
        color: #111A3A !important;
    }

    /* ESTILIZAÇÃO DO MODAL (Somente na janela popup) */
    div[role="dialog"] {
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        border: 1px solid #E1E4EC !important;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15) !important;
    }

    div[role="dialog"] * {
        color: #111A3A !important;
    }

    div[role="dialog"] code {
        background-color: #F0EBFB !important;
        color: #6331E8 !important;
    }

    div[role="dialog"] button[aria-label="Close"] {
        color: #111A3A !important;
    }
</style>
"""

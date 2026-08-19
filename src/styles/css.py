CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    #MainMenu, header, footer { visibility: hidden; }

    /* Fundo da Aplicação Principal */
    .stApp {
        background: linear-gradient(135deg, #F3F5FC 0%, #EAEFFC 50%, #F5F0FF 100%) !important;
        background-attachment: fixed !important;
        color: #111A3A !important;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 1100px !important;
    }

    /* Cartões e Envolventes */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF !important;
        border-radius: 24px !important;
        padding: 2.5rem !important;
        box-shadow: 0 12px 40px rgba(99, 49, 232, 0.06) !important;
        border: 1px solid rgba(225, 228, 236, 0.6) !important;
    }

    /* Cor padrão para rótulos e textos gerais */
    label, p, span, div {
        color: #111A3A;
    }

    /* Cabeçalho e Marca */
    .brand-logo { display: flex; align-items: center; gap: 12px; margin-bottom: 1rem; }
    .brand-logo-icon { font-size: 2rem; background: #FFFFFF; padding: 6px 12px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .brand-title { font-weight: 800; font-size: 1.25rem; color: #111A3A !important; margin: 0; line-height: 1.1; }
    .brand-subtitle { font-weight: 600; font-size: 0.75rem; color: #6331E8 !important; letter-spacing: 1px; }

    .card-header-icon { width: 52px; height: 52px; background: #F0EBFB; color: #6331E8; border-radius: 14px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; font-size: 1.6rem; }
    .main-title { text-align: center; font-weight: 800; font-size: 2.2rem; color: #111A3A !important; margin-bottom: 0.3rem; }
    .main-title span { color: #6331E8 !important; }
    .main-subtitle { text-align: center; color: #68718B !important; font-size: 0.95rem; margin-bottom: 2rem; }

    /* Estilização Geral dos Botões (Resetar, Ajuda, Ações) */
    div[data-testid="stButton"] > button {
        background-color: #FFFFFF !important;
        color: #111A3A !important;
        border: 1px solid #E1E4EC !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04) !important;
    }

    div[data-testid="stButton"] > button:hover {
        background-color: #6331E8 !important;
        color: #FFFFFF !important;
        border-color: #6331E8 !important;
        box-shadow: 0 4px 12px rgba(99, 49, 232, 0.2) !important;
    }

    div[data-testid="stButton"] > button:hover * {
        color: #FFFFFF !important;
    }

    /* Botão Primário (Ações Principais) */
    div[data-testid="stButton"] > button[kind="primary"] {
        background-color: #6331E8 !important;
        color: #FFFFFF !important;
        border: none !important;
    }

    div[data-testid="stButton"] > button[kind="primary"] * {
        color: #FFFFFF !important;
    }

    /* Entradas Numéricas e Inputs */
    div[data-baseweb="input"] { border-radius: 12px !important; border: 1px solid #E1E4EC !important; background-color: #FAFAFC !important; }
    div[data-baseweb="input"] input { color: #111A3A !important; }
    div[data-baseweb="input"]:focus-within { border-color: #6331E8 !important; background-color: #FFFFFF !important; }

    /* Janela Modal (Dialog) e Botões de Fechar */
    div[role="dialog"], 
    div[data-testid="stDialog"] {
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        border: 1px solid rgba(225, 228, 236, 0.8) !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15) !important;
    }

    div[role="dialog"] *, 
    div[data-testid="stDialog"] * {
        color: #111A3A !important;
    }

    div[role="dialog"] button[aria-label="Close"] {
        color: #111A3A !important;
    }
</style>
"""

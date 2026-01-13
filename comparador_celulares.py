# ============================================================
# COMPARADOR DE CELULARES - APPLE VS SAMSUNG 2025
# VERSÃO STREAMLIT 
# ============================================================

import streamlit as st
from datetime import datetime

# ========== CONFIGURAÇÃO DA PÁGINA ==========
st.set_page_config(
    page_title="Comparador Apple vs Samsung 2025",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== ESTILO CSS CUSTOMIZADO ==========
st.markdown("""
<style>
    /* Tema Principal */
    .main {
        background:  linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    /* Cards de Celulares */
    .celular-card {
        background:  white;
        border-radius:  15px;
        padding: 20px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease;
    }

    .celular-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }

    /* Badges */
    .badge-apple {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 5px 15px;
        border-radius:  20px;
        font-weight: bold;
        display: inline-block;
        margin: 5px 0;
    }

    .badge-samsung {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding:  5px 15px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 5px 0;
    }

    /* Métricas */
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }

    .metric-value {
        font-size: 32px;
        font-weight:  bold;
    }

    .metric-label {
        font-size:  14px;
        opacity: 0.9;
    }

    /* Título Principal */
    .main-title {
        text-align: center;
        color: white;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 10px;
        text-shadow:  2px 2px 4px rgba(0,0,0,0.3);
    }

    . subtitle {
        text-align:  center;
        color: white;
        font-size: 18px;
        margin-bottom:  30px;
        opacity: 0.9;
    }

    /* Barra de Progresso Customizada */
    .spec-bar {
        background: #e0e0e0;
        border-radius: 10px;
        height: 8px;
        margin: 5px 0;
        overflow:  hidden;
    }

    .spec-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }

    /* Botões */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    /* Divider customizado */
    .custom-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)


# ========== CLASSE CELULAR (APRIMORADA) ==========
class Celular:
    def __init__(self, marca, modelo, ram, armazenamento, bateria, camera, preco):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.armazenamento = armazenamento
        self.bateria = bateria
        self.camera = camera
        self.preco = preco

    def custo_beneficio(self):
        score = (self.ram + self.armazenamento / 10 + self.bateria / 100 + self.camera / 10) / self.preco * 10000
        return round(score, 2)

    def score_geral(self):
        return round(self.ram * 10 + self.armazenamento / 10 + self.bateria / 10 + self.camera / 2, 2)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

    def get_badge_class(self):
        return "badge-apple" if self.marca == "Apple" else "badge-samsung"

    def get_emoji(self):
        return "🍎" if self.marca == "Apple" else "📱"


# ========== DADOS DOS CELULARES ==========
cel1 = Celular("Apple", "iPhone 15 Pro Max", 8, 256, 4422, 48, 7999)
cel2 = Celular("Apple", "iPhone 15", 6, 128, 3349, 48, 4999)
cel3 = Celular("Apple", "iPhone SE", 4, 64, 2018, 12, 2999)

cel4 = Celular("Samsung", "Galaxy S24 Ultra", 12, 512, 5000, 200, 7499)
cel5 = Celular("Samsung", "Galaxy S24", 8, 256, 4000, 50, 4999)
cel6 = Celular("Samsung", "Galaxy A54", 8, 256, 5000, 50, 2499)

celulares = [cel1, cel2, cel3, cel4, cel5, cel6]
apple_phones = [cel1, cel2, cel3]
samsung_phones = [cel4, cel5, cel6]


# ========== FUNÇÕES AUXILIARES ==========
def render_spec_bar(value, max_value, color="#667eea"):
    """Renderiza uma barra de progresso para especificações"""
    percentage = (value / max_value) * 100
    return f"""
    <div class="spec-bar">
        <div class="spec-fill" style="width:  {percentage}%; background: {color};"></div>
    </div>
    """


def render_celular_card(cel, show_comparison=False):
    """Renderiza um card bonito para o celular"""
    badge_class = cel.get_badge_class()
    emoji = cel.get_emoji()

    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown(f"<div style='font-size: 80px; text-align: center;'>{emoji}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f'<span class="{badge_class}">{cel.marca}</span>', unsafe_allow_html=True)
        st.markdown(f"### {cel.modelo}")

        # Métricas em colunas
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("RAM", f"{cel.ram}GB", delta=None)
        with c2:
            st.metric("Armazenamento", f"{cel.armazenamento}GB")
        with c3:
            st.metric("Bateria", f"{cel.bateria}mAh")
        with c4:
            st.metric("Câmera", f"{cel.camera}MP")

        # Score e C/B
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("💰 Preço", f"R$ {cel.preco:,.2f}")
        with c2:
            st.metric("⭐ Score", f"{cel.score_geral()}")
        with c3:
            st.metric("💎 C/B", f"{cel.custo_beneficio()}")

    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)


def render_comparison_bars(cel):
    """Renderiza barras de comparação para especificações"""
    max_ram = max(c.ram for c in celulares)
    max_storage = max(c.armazenamento for c in celulares)
    max_battery = max(c.bateria for c in celulares)
    max_camera = max(c.camera for c in celulares)

    st.markdown(f"**RAM:** {cel.ram}GB")
    st.markdown(render_spec_bar(cel.ram, max_ram, "#667eea"), unsafe_allow_html=True)

    st.markdown(f"**Armazenamento:** {cel.armazenamento}GB")
    st.markdown(render_spec_bar(cel.armazenamento, max_storage, "#764ba2"), unsafe_allow_html=True)

    st.markdown(f"**Bateria:** {cel.bateria}mAh")
    st.markdown(render_spec_bar(cel.bateria, max_battery, "#f093fb"), unsafe_allow_html=True)

    st.markdown(f"**Câmera:** {cel.camera}MP")
    st.markdown(render_spec_bar(cel.camera, max_camera, "#f5576c"), unsafe_allow_html=True)


# ========== HEADER ==========
st.markdown('<h1 class="main-title">📱 Comparador de Celulares 2025</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Apple 🍎 vs Samsung 📱 | Análise Completa de Specs & Custo-Benefício</p>',
            unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/smartphone-tablet.png", width=100)
    st.title("🎯 Menu Principal")

    menu = st.radio(
        "Escolha uma opção:",
        [
            "🏠 Início",
            "🔥 Comparar TOP 3",
            "🏆 Ver Rankings",
            "⚔️ Duelo 1 vs 1",
            "📋 Todos os Celulares",
            "🥇 Melhores Specs",
            "📊 Resumo Geral"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.caption(f"📅 Atualizado em: {datetime.now().strftime('%d/%m/%Y')}")
    st.caption("Desenvolvido por Bima tech")

# ========== PÁGINA INICIAL ==========
if menu == "🏠 Início":
    st.balloons()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">6</div>
            <div class="metric-label">📱 Celulares</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">2</div>
            <div class="metric-label">🏢 Marcas</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">5</div>
            <div class="metric-label">📊 Análises</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🎯 Bem-vindo ao Comparador!")
    st.info("""
    👉 Use o menu lateral para navegar pelas opções: 
    - **🔥 Comparar TOP 3**:  Veja os 3 melhores de cada marca
    - **🏆 Rankings**: TOP 2 em performance e custo-benefício
    - **⚔️ Duelo 1 vs 1**: iPhone 15 Pro Max vs Galaxy S24 Ultra
    - **📋 Todos**:  Lista completa com detalhes
    - **🥇 Specs**: Campeões em cada categoria
    - **📊 Resumo**:  Apple vs Samsung - Quem vence?
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.success("🍎 **Apple** - Design premium e ecossistema integrado")
        for cel in apple_phones:
            st.write(f"• {cel.modelo} - R$ {cel.preco:,. 2f}")

    with col2:
        st.error("📱 **Samsung** - Inovação e custo-benefício")
        for cel in samsung_phones:
            st.write(f"• {cel.modelo} - R$ {cel.preco:,.2f}")


# ========== COMPARAR TOP 3 ==========
elif menu == "🔥 Comparar TOP 3":
    st.header("🔥 TOP 3 de Linha - Apple vs Samsung")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🍎 Apple")
        for cel in apple_phones:
            render_celular_card(cel)

    with col2:
        st.subheader("📱 Samsung")
        for cel in samsung_phones:
            render_celular_card(cel)


# ========== RANKINGS ==========
elif menu == "🏆 Ver Rankings":
    st.header("🏆 Rankings - Os Melhores dos Melhores")

    tab1, tab2 = st.tabs(["⭐ Melhor Score Geral", "💎 Melhor Custo-Benefício"])

    with tab1:
        st.subheader("TOP 2 - Maior Score Técnico")
        top_score = sorted(celulares, key=lambda x: x.score_geral(), reverse=True)[:2]

        for i, cel in enumerate(top_score, 1):
            medal = "🥇" if i == 1 else "🥈"
            st.markdown(f"### {medal} {i}º Lugar:  {cel}")
            render_celular_card(cel)

    with tab2:
        st.subheader("TOP 2 - Melhor Relação Qualidade/Preço")
        top_cb = sorted(celulares, key=lambda x: x.custo_beneficio(), reverse=True)[:2]

        for i, cel in enumerate(top_cb, 1):
            medal = "🥇" if i == 1 else "🥈"
            st.markdown(f"### {medal} {i}º Lugar: {cel}")
            render_celular_card(cel)


# ========== DUELO 1 VS 1 ==========
elif menu == "⚔️ Duelo 1 vs 1":
    st.header("⚔️ Duelo Épico:  Tops de Linha")
    st.subheader("iPhone 15 Pro Max 🍎 vs 📱 Galaxy S24 Ultra")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🍎 iPhone 15 Pro Max")
        st.markdown('<span class="badge-apple">Apple</span>', unsafe_allow_html=True)
        st.markdown("---")
        render_comparison_bars(cel1)
        st.markdown("---")
        st.metric("💰 Preço", f"R$ {cel1.preco:,.2f}")
        st.metric("⭐ Score Geral", f"{cel1.score_geral()}")
        st.metric("💎 Custo-Benefício", f"{cel1.custo_beneficio()}")

    with col2:
        st.markdown("### 📱 Galaxy S24 Ultra")
        st.markdown('<span class="badge-samsung">Samsung</span>', unsafe_allow_html=True)
        st.markdown("---")
        render_comparison_bars(cel4)
        st.markdown("---")
        st.metric("💰 Preço", f"R$ {cel4.preco:,.2f}")
        st.metric("⭐ Score Geral", f"{cel4.score_geral()}")
        st.metric("💎 Custo-Benefício", f"{cel4.custo_beneficio()}")

    st.markdown("---")

    vencedor = cel1 if cel1.score_geral() > cel4.score_geral() else cel4
    diferenca = abs(cel1.score_geral() - cel4.score_geral())

    if vencedor == cel1:
        st.success(f"🏆 **VENCEDOR:  {vencedor}** com {diferenca} pontos de diferença!")
    else:
        st.error(f"🏆 **VENCEDOR: {vencedor}** com {diferenca} pontos de diferença!")


# ========== TODOS OS CELULARES ==========
elif menu == "📋 Todos os Celulares":
    st.header("📋 Catálogo Completo - 6 Modelos Disponíveis")

    # Filtro
    filtro_marca = st.multiselect(
        "Filtrar por marca:",
        ["Apple", "Samsung"],
        default=["Apple", "Samsung"]
    )

    celulares_filtrados = [c for c in celulares if c.marca in filtro_marca]

    for cel in celulares_filtrados:
        with st.expander(f"{cel.get_emoji()} {cel}", expanded=False):
            render_celular_card(cel)


# ========== MELHORES SPECS ==========
elif menu == "🥇 Melhores Specs":
    st.header("🥇 Campeões por Categoria")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Maior RAM")
        cel_ram = max(celulares, key=lambda x: x.ram)
        st.success(f"**{cel_ram}** - {cel_ram.ram}GB")

        st.subheader("💾 Maior Armazenamento")
        cel_storage = max(celulares, key=lambda x: x.armazenamento)
        st.success(f"**{cel_storage}** - {cel_storage.armazenamento}GB")

        st.subheader("🔋 Melhor Bateria")
        cel_battery = max(celulares, key=lambda x: x.bateria)
        st.success(f"**{cel_battery}** - {cel_battery.bateria}mAh")

    with col2:
        st.subheader("📸 Melhor Câmera")
        cel_camera = max(celulares, key=lambda x: x.camera)
        st.success(f"**{cel_camera}** - {cel_camera.camera}MP")

        st.subheader("💰 Mais Barato")
        cel_cheap = min(celulares, key=lambda x: x.preco)
        st.success(f"**{cel_cheap}** - R$ {cel_cheap.preco:,.2f}")

        st.subheader("💎 Melhor C/B")
        cel_cb = max(celulares, key=lambda x: x.custo_beneficio())
        st.success(f"**{cel_cb}** - {cel_cb.custo_beneficio()} pontos")


# ========== RESUMO GERAL ==========
elif menu == "📊 Resumo Geral":
    st.header("📊 Resumo Geral - Apple 🆚 Samsung")

    media_score_apple = sum(c.score_geral() for c in apple_phones) / len(apple_phones)
    media_score_samsung = sum(c.score_geral() for c in samsung_phones) / len(samsung_phones)

    media_cb_apple = sum(c.custo_beneficio() for c in apple_phones) / len(apple_phones)
    media_cb_samsung = sum(c.custo_beneficio() for c in samsung_phones) / len(samsung_phones)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🍎 Apple")
        st.metric("Score Médio", f"{media_score_apple:.2f}", delta=None)
        st.metric("C/B Médio", f"{media_cb_apple:.2f}")
        st.metric("Preço Médio", f"R$ {sum(c.preco for c in apple_phones) / len(apple_phones):,.2f}")

    with col2:
        st.markdown("### 📱 Samsung")
        st.metric("Score Médio", f"{media_score_samsung:.2f}", delta=None)
        st.metric("C/B Médio", f"{media_cb_samsung:. 2f}")
        st.metric("Preço Médio", f"R$ {sum(c.preco for c in samsung_phones) / len(samsung_phones):,.2f}")

    st.markdown("---")

    # Vencedor por Score
    if media_score_apple > media_score_samsung:
        st.success(f"🏆 **VENCEDOR EM PERFORMANCE:** Apple com {media_score_apple:. 2f} pontos!")
    else:
        st.error(f"🏆 **VENCEDOR EM PERFORMANCE:** Samsung com {media_score_samsung:. 2f} pontos!")

    # Vencedor por C/B
    if media_cb_apple > media_cb_samsung:
        st.success(f"💎 **VENCEDOR EM CUSTO-BENEFÍCIO:** Apple com {media_cb_apple:.2f} pontos!")
    else:
        st.error(f"💎 **VENCEDOR EM CUSTO-BENEFÍCIO:** Samsung com {media_cb_samsung:.2f} pontos!")

    # Gráfico de comparação
    st.markdown("### 📈 Comparação Visual")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Score Geral:**")
        st.markdown(render_spec_bar(media_score_apple, max(media_score_apple, media_score_samsung), "#667eea"),
                    unsafe_allow_html=True)
        st.caption(f"Apple: {media_score_apple:.2f}")

        st.markdown(render_spec_bar(media_score_samsung, max(media_score_apple, media_score_samsung), "#f5576c"),
                    unsafe_allow_html=True)
        st.caption(f"Samsung: {media_score_samsung:.2f}")

    with col2:
        st.markdown("**Custo-Benefício:**")
        st.markdown(render_spec_bar(media_cb_apple, max(media_cb_apple, media_cb_samsung), "#667eea"),
                    unsafe_allow_html=True)
        st.caption(f"Apple: {media_cb_apple:.2f}")

        st.markdown(render_spec_bar(media_cb_samsung, max(media_cb_apple, media_cb_samsung), "#f5576c"),
                    unsafe_allow_html=True)
        st.caption(f"Samsung: {media_cb_samsung:. 2f}")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white; padding: 20px;'>
    <p style='font-size: 14px;'>
        Desenvolvido  por <strong>Abimael de Menezes Pedro / BIMA TECH</strong><br>
        🌐 <a href='https://www.abimaeldev.eng.br/' style='color: white;'>abimaeldev.eng.br</a> | 
        💼 <a href='https://www.linkedin.com/in/bimadevfull/' style='color: white;'>LinkedIn</a> | 
        🐙 <a href='https://github.com/bimadevfull' style='color: white;'>GitHub</a>
    </p>
    <p style='font-size:  12px; opacity: 0.8;'>
        📱 Comparador de Celulares 2025 | Versão 2.0 Premium
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# COMPARADOR DE CELULARES - APPLE VS SAMSUNG 2025
# VERSÃO STREAMLIT (PC / WEB)
# ============================================================

import streamlit as st

# ========== CLASSE CELULAR (MANTIDA) ==========
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
        score = (self.ram + self.armazenamento/10 + self.bateria/100 + self.camera/10) / self.preco * 10000
        return round(score, 2)
    
    def score_geral(self):
        return round(self.ram * 10 + self.armazenamento/10 + self.bateria/10 + self.camera/2, 2)
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"

# ========== CELULARES ==========
cel1 = Celular("Apple", "iPhone 15 Pro Max", 8, 256, 4422, 48, 7999)
cel2 = Celular("Apple", "iPhone 15", 6, 128, 3349, 48, 4999)
cel3 = Celular("Apple", "iPhone SE", 4, 64, 2018, 12, 2999)

cel4 = Celular("Samsung", "Galaxy S24 Ultra", 12, 512, 5000, 200, 7499)
cel5 = Celular("Samsung", "Galaxy S24", 8, 256, 4000, 50, 4999)
cel6 = Celular("Samsung", "Galaxy A54", 8, 256, 5000, 50, 2499)

celulares = [cel1, cel2, cel3, cel4, cel5, cel6]

# ========== INTERFACE ==========
st.set_page_config(page_title="Comparador Apple vs Samsung", layout="centered")

st.title("📱 Comparador de Celulares – Apple vs Samsung 2025")
st.write("Projeto convertido do SPIKE Prime para Streamlit, mantendo a lógica original.")

menu = st.sidebar.selectbox(
    "Menu",
    (
        "Comparar TOP 3",
        "Ver Rankings",
        "Comparação 1 vs 1",
        "Todos os Celulares",
        "Melhores Specs",
        "Resumo Geral"
    )
)

# ========== FUNÇÕES ==========

def comparar_top_3():
    st.header("TOP 3 – Apple")
    for cel in [cel1, cel2, cel3]:
        st.write(f"**{cel}**")
        st.write(f"RAM: {cel.ram}GB | Bateria: {cel.bateria}mAh | Câmera: {cel.camera}MP")
        st.write(f"Score: {cel.score_geral()} | C/B: {cel.custo_beneficio()}")
        st.write(f"Preço: R$ {cel.preco:,.2f}")
        st.divider()

    st.header("TOP 3 – Samsung")
    for cel in [cel4, cel5, cel6]:
        st.write(f"**{cel}**")
        st.write(f"RAM: {cel.ram}GB | Bateria: {cel.bateria}mAh | Câmera: {cel.camera}MP")
        st.write(f"Score: {cel.score_geral()} | C/B: {cel.custo_beneficio()}")
        st.write(f"Preço: R$ {cel.preco:,.2f}")
        st.divider()


def mostrar_rankings():
    st.header("Rankings")

    st.subheader("TOP 2 – Melhor Score Geral")
    top_score = sorted(celulares, key=lambda x: x.score_geral(), reverse=True)[:2]
    for cel in top_score:
        st.write(f"{cel} – Score: {cel.score_geral()}")

    st.subheader("TOP 2 – Melhor Custo-Benefício")
    top_cb = sorted(celulares, key=lambda x: x.custo_beneficio(), reverse=True)[:2]
    for cel in top_cb:
        st.write(f"{cel} – C/B: {cel.custo_beneficio()}")


def comparacao_1v1():
    st.header("Comparação 1 vs 1")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(str(cel1))
        st.write(f"RAM: {cel1.ram}GB")
        st.write(f"Armazenamento: {cel1.armazenamento}GB")
        st.write(f"Bateria: {cel1.bateria}mAh")
        st.write(f"Câmera: {cel1.camera}MP")
        st.write(f"Score: {cel1.score_geral()}")

    with col2:
        st.subheader(str(cel4))
        st.write(f"RAM: {cel4.ram}GB")
        st.write(f"Armazenamento: {cel4.armazenamento}GB")
        st.write(f"Bateria: {cel4.bateria}mAh")
        st.write(f"Câmera: {cel4.camera}MP")
        st.write(f"Score: {cel4.score_geral()}")

    vencedor = cel1 if cel1.score_geral() > cel4.score_geral() else cel4
    st.success(f"Vencedor: {vencedor}")


def todos_celulares():
    st.header("Todos os Celulares")
    for cel in celulares:
        st.write(f"**{cel}**")
        st.write(f"RAM: {cel.ram}GB | Armazenamento: {cel.armazenamento}GB")
        st.write(f"Bateria: {cel.bateria}mAh | Câmera: {cel.camera}MP")
        st.write(f"Preço: R$ {cel.preco:,.2f}")
        st.write(f"Score: {cel.score_geral()} | C/B: {cel.custo_beneficio()}")
        st.divider()


def melhores_specs():
    st.header("Melhores Especificações")
    st.write(f"Maior RAM: {max(celulares, key=lambda x: x.ram)}")
    st.write(f"Maior Armazenamento: {max(celulares, key=lambda x: x.armazenamento)}")
    st.write(f"Melhor Bateria: {max(celulares, key=lambda x: x.bateria)}")
    st.write(f"Melhor Câmera: {max(celulares, key=lambda x: x.camera)}")
    st.write(f"Mais Barato: {min(celulares, key=lambda x: x.preco)}")


def resumo_geral():
    st.header("Resumo Geral")

    apple = [cel1, cel2, cel3]
    samsung = [cel4, cel5, cel6]

    media_score_apple = sum(c.score_geral() for c in apple) / len(apple)
    media_score_samsung = sum(c.score_geral() for c in samsung) / len(samsung)

    st.write(f"Score médio Apple: {media_score_apple:.2f}")
    st.write(f"Score médio Samsung: {media_score_samsung:.2f}")

    vencedor = "Apple" if media_score_apple > media_score_samsung else "Samsung"
    st.success(f"Melhor score médio: {vencedor}")

# ========== EXECUÇÃO ==========
if menu == "Comparar TOP 3":
    comparar_top_3()
elif menu == "Ver Rankings":
    mostrar_rankings()
elif menu == "Comparação 1 vs 1":
    comparacao_1v1()
elif menu == "Todos os Celulares":
    todos_celulares()
elif menu == "Melhores Specs":
    melhores_specs()
elif menu == "Resumo Geral":
    resumo_geral()

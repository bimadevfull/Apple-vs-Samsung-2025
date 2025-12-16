# Comparador de Celulares - Apple vs Samsung 2025
import time
import os
from typing import List

class Celular:
    def __init__(self, marca, modelo, processador, ram, armazenamento, bateria, 
                 camera_principal, tela, preco, vendas, is_top_linha=False):
        self.marca = marca
        self.modelo = modelo
        self.processador = processador
        self.ram = ram
        self.armazenamento = armazenamento
        self.bateria = bateria
        self. camera_principal = camera_principal
        self.tela = tela
        self.preco = preco
        self.vendas = vendas
        self.is_top_linha = is_top_linha
        
    def custo_beneficio(self):
        """Calcula score de custo-benefício baseado nas specs"""
        score = (self. ram + self.armazenamento/10 + self.bateria/100 + 
                 self.camera_principal/10 + float(self.tela)) / self.preco * 10000
        return round(score, 2)
    
    def score_geral(self):
        """Calcula score geral baseado nas especificações"""
        return round(self.ram * 10 + self.armazenamento/10 + self. bateria/10 + 
                     self.camera_principal/2 + float(self.tela) * 15, 2)
    
    def score_bateria(self):
        """Score baseado na bateria"""
        return round(self.bateria / 100, 2)
    
    def score_camera(self):
        """Score baseado na câmera"""
        return round(self.camera_principal / 2, 2)
    
    def categoria_preco(self):
        """Retorna a categoria de preço do celular"""
        if self. preco >= 7000:
            return "💎 Premium"
        elif self.preco >= 4500:
            return "⭐ Alto"
        elif self.preco >= 2500:
            return "🔵 Médio"
        else:
            return "💚 Econômico"
    
    def detalhes_completos(self):
        """Retorna string formatada com todos os detalhes"""
        return f"""
    ╔{'═' * 76}╗
    ║  {self.marca} {self.modelo:<65} ║
    ╠{'═' * 76}╣
    ║  🔧 Processador:       {self.processador:<54} ║
    ║  💾 RAM:              {self.ram}GB{' ' * (59 - len(str(self.ram)))} ║
    ║  📦 Armazenamento:    {self.armazenamento}GB{' ' * (57 - len(str(self. armazenamento)))} ║
    ║  🔋 Bateria:          {self.bateria}mAh{' ' * (55 - len(str(self. bateria)))} ║
    ║  📷 Câmera:           {self.camera_principal}MP{' ' * (57 - len(str(self. camera_principal)))} ║
    ║  📱 Tela:             {self.tela}\"{' ' * (58 - len(str(self. tela)))} ║
    ║  💰 Preço:            R$ {self. preco:,.2f}{' ' * (51 - len(f'{self.preco:,.2f}'))} ║
    ║  📊 Vendas:            {self.vendas:,} unidades{' ' * (44 - len(f'{self.vendas:,}'))} ║
    ║  🏷️  Categoria:        {self.categoria_preco()}{' ' * (52 - len(self.categoria_preco()))} ║
    ║  ⭐ Score Geral:      {self.score_geral()}{' ' * (57 - len(str(self.score_geral())))} ║
    ║  💎 Custo-Benefício:  {self.custo_beneficio()}{' ' * (57 - len(str(self. custo_beneficio())))} ║
    ╚{'═' * 76}╝
        """
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"


# ========== CELULARES APPLE (5 modelos) ==========
apple_phones = [
    Celular(
        marca="Apple",
        modelo="iPhone 15 Pro Max",
        processador="A17 Pro",
        ram=8,
        armazenamento=256,
        bateria=4422,
        camera_principal=48,
        tela=6.7,
        preco=7999,
        vendas=15000000,
        is_top_linha=True
    ),
    Celular(
        marca="Apple",
        modelo="iPhone 15 Pro",
        processador="A17 Pro",
        ram=8,
        armazenamento=256,
        bateria=3274,
        camera_principal=48,
        tela=6.1,
        preco=6999,
        vendas=12000000,
        is_top_linha=True
    ),
    Celular(
        marca="Apple",
        modelo="iPhone 15 Plus",
        processador="A16 Bionic",
        ram=6,
        armazenamento=128,
        bateria=4383,
        camera_principal=48,
        tela=6.7,
        preco=5999,
        vendas=8000000,
        is_top_linha=True
    ),
    Celular(
        marca="Apple",
        modelo="iPhone 15",
        processador="A16 Bionic",
        ram=6,
        armazenamento=128,
        bateria=3349,
        camera_principal=48,
        tela=6.1,
        preco=4999,
        vendas=18000000
    ),
    Celular(
        marca="Apple",
        modelo="iPhone SE (2025)",
        processador="A15 Bionic",
        ram=4,
        armazenamento=64,
        bateria=2018,
        camera_principal=12,
        tela=4.7,
        preco=2999,
        vendas=5000000
    )
]

# ========== CELULARES SAMSUNG (8 modelos) ==========
samsung_phones = [
    Celular(
        marca="Samsung",
        modelo="Galaxy S24 Ultra",
        processador="Snapdragon 8 Gen 3",
        ram=12,
        armazenamento=512,
        bateria=5000,
        camera_principal=200,
        tela=6.8,
        preco=7499,
        vendas=14000000,
        is_top_linha=True
    ),
    Celular(
        marca="Samsung",
        modelo="Galaxy S24+",
        processador="Snapdragon 8 Gen 3",
        ram=12,
        armazenamento=256,
        bateria=4900,
        camera_principal=50,
        tela=6.7,
        preco=5999,
        vendas=10000000,
        is_top_linha=True
    ),
    Celular(
        marca="Samsung",
        modelo="Galaxy S24",
        processador="Snapdragon 8 Gen 3",
        ram=8,
        armazenamento=256,
        bateria=4000,
        camera_principal=50,
        tela=6.2,
        preco=4999,
        vendas=13000000,
        is_top_linha=True
    ),
    Celular(
        marca="Samsung",
        modelo="Galaxy Z Fold 5",
        processador="Snapdragon 8 Gen 2",
        ram=12,
        armazenamento=512,
        bateria=4400,
        camera_principal=50,
        tela=7.6,
        preco=9999,
        vendas=3000000
    ),
    Celular(
        marca="Samsung",
        modelo="Galaxy Z Flip 5",
        processador="Snapdragon 8 Gen 2",
        ram=8,
        armazenamento=256,
        bateria=3700,
        camera_principal=12,
        tela=6.7,
        preco=5499,
        vendas=6000000
    ),
    Celular(
        marca="Samsung",
        modelo="Galaxy A54",
        processador="Exynos 1380",
        ram=8,
        armazenamento=256,
        bateria=5000,
        camera_principal=50,
        tela=6.4,
        preco=2499,
        vendas=20000000
    ),
    Celular(
        marca="Samsung",
        modelo="Galaxy A34",
        processador="Dimensity 1080",
        ram=6,
        armazenamento=128,
        bateria=5000,
        camera_principal=48,
        tela=6.6,
        preco=1799,
        vendas=15000000
    ),
    Celular(
        marca="Samsung",
        modelo="Galaxy M54",
        processador="Exynos 1380",
        ram=8,
        armazenamento=256,
        bateria=6000,
        camera_principal=108,
        tela=6.7,
        preco=2199,
        vendas=12000000
    )
]

# Combinar todos os celulares
todos_celulares = apple_phones + samsung_phones


# ========== FUNÇÕES DE UTILIDADE ==========
def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa a execução até o usuário pressionar Enter"""
    input("\n🔄 Pressione ENTER para continuar...")

def animacao_carregando(mensagem="Carregando", duracao=1.5):
    """Exibe uma animação de carregamento"""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    fim = time.time() + duracao
    i = 0
    while time. time() < fim:
        print(f"\r{mensagem} {frames[i % len(frames)]}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r{mensagem} ✓")

def titulo(texto, estilo="duplo"):
    """Exibe um título formatado"""
    largura = 80
    if estilo == "duplo":
        print("\n╔" + "═" * (largura - 2) + "╗")
        print("║" + texto.center(largura - 2) + "║")
        print("╚" + "═" * (largura - 2) + "╝\n")
    elif estilo == "simples": 
        print("\n┌" + "─" * (largura - 2) + "┐")
        print("│" + texto.center(largura - 2) + "│")
        print("└" + "─" * (largura - 2) + "┘\n")
    else:
        print("\n" + "=" * largura)
        print(texto. center(largura))
        print("=" * largura + "\n")

def barra_progresso(valor, maximo, largura=40, label=""):
    """Exibe uma barra de progresso"""
    percentual = (valor / maximo) * 100
    preenchido = int((valor / maximo) * largura)
    barra = "█" * preenchido + "░" * (largura - preenchido)
    print(f"{label: <20} [{barra}] {percentual: >5.1f}%")


# ========== COMPARAÇÃO DOS 3 TOP DE LINHA ==========
def comparar_top_de_linha():
    titulo("🔥 COMPARAÇÃO - TOP DE LINHA (3 de cada marca)", "duplo")
    
    apple_top = [phone for phone in apple_phones if phone.is_top_linha]
    samsung_top = [phone for phone in samsung_phones if phone. is_top_linha]
    
    print("📱 " + "APPLE - TOP 3". center(76) + "\n")
    for i, phone in enumerate(apple_top, 1):
        print(f"🍎 {i}º - {phone.modelo}")
        print(f"├─ 🔧 Processador: {phone.processador}")
        print(f"├─ 💾 RAM: {phone.ram}GB | 📦 Armazenamento: {phone.armazenamento}GB")
        print(f"├─ 🔋 Bateria: {phone. bateria}mAh | 📷 Câmera:  {phone.camera_principal}MP")
        print(f"├─ 📱 Tela: {phone.tela}\" | 💰 Preço: R$ {phone.preco:,.2f}")
        print(f"├─ 📊 Vendas: {phone.vendas:,} unidades")
        print(f"└─ ⭐ Score:  {phone.score_geral()} | 💎 C/B: {phone.custo_beneficio()}\n")
    
    print("\n" + "─" * 80 + "\n")
    
    print("📱 " + "SAMSUNG - TOP 3". center(76) + "\n")
    for i, phone in enumerate(samsung_top, 1):
        print(f"📱 {i}º - {phone.modelo}")
        print(f"├─ 🔧 Processador: {phone.processador}")
        print(f"├─ 💾 RAM: {phone.ram}GB | 📦 Armazenamento: {phone.armazenamento}GB")
        print(f"├─ 🔋 Bateria:  {phone.bateria}mAh | 📷 Câmera: {phone.camera_principal}MP")
        print(f"├─ 📱 Tela: {phone. tela}\" | 💰 Preço: R$ {phone.preco:,.2f}")
        print(f"├─ 📊 Vendas: {phone.vendas:,} unidades")
        print(f"└─ ⭐ Score: {phone. score_geral()} | 💎 C/B: {phone.custo_beneficio()}\n")


# ========== RANKINGS ==========
def mostrar_rankings():
    titulo("🏆 RANKINGS E ANÁLISES", "duplo")
    
    # TOP 2 - MAIOR VENDA
    print("\n💰 TOP 2 - MAIORES VENDAS\n" + "─" * 80)
    top_vendas = sorted(todos_celulares, key=lambda x: x.vendas, reverse=True)[:2]
    for i, phone in enumerate(top_vendas, 1):
        print(f"\n🥇 {i}º lugar:  {phone}")
        print(f"   📊 Vendas: {phone. vendas:,} unidades")
        print(f"   💰 Preço: R$ {phone.preco:,.2f}")
        barra_progresso(phone.vendas, top_vendas[0].vendas, label="   Performance")
    
    # TOP 2 - MELHORES CELULARES (por score geral)
    print("\n\n⭐ TOP 2 - MELHORES CELULARES (Score Geral)\n" + "─" * 80)
    top_melhores = sorted(todos_celulares, key=lambda x:  x.score_geral(), reverse=True)[:2]
    for i, phone in enumerate(top_melhores, 1):
        print(f"\n🥇 {i}º lugar: {phone}")
        print(f"   ⭐ Score Geral: {phone.score_geral()}")
        print(f"   🔧 Specs: {phone.ram}GB RAM, {phone.armazenamento}GB, {phone.bateria}mAh, {phone.camera_principal}MP")
        print(f"   💰 Preço: R$ {phone.preco:,. 2f}")
        barra_progresso(phone.score_geral(), top_melhores[0].score_geral(), label="   Score")
    
    # TOP 2 - MELHOR CUSTO-BENEFÍCIO
    print("\n\n💎 TOP 2 - MELHOR CUSTO-BENEFÍCIO\n" + "─" * 80)
    top_custo_beneficio = sorted(todos_celulares, key=lambda x:  x.custo_beneficio(), reverse=True)[:2]
    for i, phone in enumerate(top_custo_beneficio, 1):
        print(f"\n🥇 {i}º lugar: {phone}")
        print(f"   💎 Score C/B: {phone.custo_beneficio()}")
        print(f"   💰 Preço: R$ {phone.preco:,.2f}")
        print(f"   🔧 Specs: {phone.ram}GB RAM, {phone.armazenamento}GB, {phone.camera_principal}MP")
        barra_progresso(phone.custo_beneficio(), top_custo_beneficio[0].custo_beneficio(), label="   Custo-Benefício")


# ========== NOVA:  COMPARAÇÃO DIRETA 1x1 ==========
def comparacao_direta():
    titulo("⚔️ COMPARAÇÃO DIRETA - 1 vs 1", "duplo")
    
    print("Selecione dois celulares para comparar:\n")
    
    print("🍎 APPLE:")
    for i, phone in enumerate(apple_phones, 1):
        print(f"  {i}.  {phone.modelo} - R$ {phone.preco:,.2f}")
    
    print("\n📱 SAMSUNG:")
    for i, phone in enumerate(samsung_phones, len(apple_phones) + 1):
        print(f"  {i}. {phone.modelo} - R$ {phone.preco:,.2f}")
    
    try:
        escolha1 = int(input("\nEscolha o primeiro celular (número): ")) - 1
        escolha2 = int(input("Escolha o segundo celular (número): ")) - 1
        
        cel1 = todos_celulares[escolha1]
        cel2 = todos_celulares[escolha2]
        
        animacao_carregando("Comparando dispositivos")
        
        titulo(f"⚔️ {cel1} VS {cel2}", "simples")
        
        print(f"\n{'ESPECIFICAÇÃO':<25} {'CELULAR 1':<25} {'CELULAR 2':<25} {'VENCEDOR':<10}")
        print("─" * 85)
        
        # Processador
        print(f"{'🔧 Processador': <25} {cel1.processador:<25} {cel2.processador:<25} {'─':<10}")
        
        # RAM
        vencedor = "✓ C1" if cel1.ram > cel2.ram else "✓ C2" if cel2.ram > cel1.ram else "Empate"
        print(f"{'💾 RAM':<25} {str(cel1.ram) + 'GB':<25} {str(cel2.ram) + 'GB':<25} {vencedor:<10}")
        
        # Armazenamento
        vencedor = "✓ C1" if cel1.armazenamento > cel2.armazenamento else "✓ C2" if cel2.armazenamento > cel1.armazenamento else "Empate"
        print(f"{'📦 Armazenamento':<25} {str(cel1.armazenamento) + 'GB':<25} {str(cel2.armazenamento) + 'GB':<25} {vencedor:<10}")
        
        # Bateria
        vencedor = "✓ C1" if cel1.bateria > cel2.bateria else "✓ C2" if cel2.bateria > cel1.bateria else "Empate"
        print(f"{'🔋 Bateria':<25} {str(cel1.bateria) + 'mAh':<25} {str(cel2.bateria) + 'mAh':<25} {vencedor:<10}")
        
        # Câmera
        vencedor = "✓ C1" if cel1.camera_principal > cel2.camera_principal else "✓ C2" if cel2.camera_principal > cel1.camera_principal else "Empate"
        print(f"{'📷 Câmera':<25} {str(cel1.camera_principal) + 'MP':<25} {str(cel2.camera_principal) + 'MP':<25} {vencedor: <10}")
        
        # Tela
        vencedor = "✓ C1" if cel1.tela > cel2.tela else "✓ C2" if cel2.tela > cel1.tela else "Empate"
        print(f"{'📱 Tela':<25} {str(cel1.tela) + '\"':<25} {str(cel2.tela) + '\"':<25} {vencedor:<10}")
        
        # Preço
        vencedor = "✓ C1" if cel1.preco < cel2.preco else "✓ C2" if cel2.preco < cel1.preco else "Empate"
        print(f"{'💰 Preço':<25} {'R$ ' + f'{cel1.preco:,. 2f}':<25} {'R$ ' + f'{cel2.preco:,.2f}': <25} {vencedor:<10}")
        
        # Score
        vencedor = "✓ C1" if cel1.score_geral() > cel2.score_geral() else "✓ C2" if cel2.score_geral() > cel1.score_geral() else "Empate"
        print(f"{'⭐ Score Geral':<25} {str(cel1.score_geral()):<25} {str(cel2.score_geral()):<25} {vencedor: <10}")
        
        # Custo-Benefício
        vencedor = "✓ C1" if cel1.custo_beneficio() > cel2.custo_beneficio() else "✓ C2" if cel2.custo_beneficio() > cel1.custo_beneficio() else "Empate"
        print(f"{'💎 Custo-Benefício':<25} {str(cel1.custo_beneficio()):<25} {str(cel2.custo_beneficio()):<25} {vencedor:<10}")
        
    except (ValueError, IndexError):
        print("\n❌ Escolha inválida! Tente novamente.")


# ========== NOVA: BUSCAR POR ORÇAMENTO ==========
def buscar_por_orcamento():
    titulo("💰 BUSCAR CELULAR POR ORÇAMENTO", "duplo")
    
    try:
        orcamento = float(input("Digite seu orçamento máximo (R$): "))
        
        animacao_carregando("Buscando opções", 1)
        
        opcoes = [phone for phone in todos_celulares if phone.preco <= orcamento]
        
        if not opcoes:
            print(f"\n❌ Nenhum celular encontrado até R$ {orcamento:,. 2f}")
            return
        
        # Ordenar por custo-benefício
        opcoes.sort(key=lambda x: x.custo_beneficio(), reverse=True)
        
        print(f"\n✅ Encontrados {len(opcoes)} celulares dentro do seu orçamento:\n")
        print("─" * 80)
        
        for i, phone in enumerate(opcoes, 1):
            print(f"\n{i}. {phone} - {phone.categoria_preco()}")
            print(f"   💰 Preço: R$ {phone.preco:,.2f}")
            print(f"   💎 Custo-Benefício: {phone.custo_beneficio()}")
            print(f"   🔧 {phone.ram}GB RAM, {phone.armazenamento}GB, {phone.bateria}mAh, {phone.camera_principal}MP")
            
    except ValueError:
        print("\n❌ Valor inválido! Digite apenas números.")


# ========== NOVA: FILTRAR POR CATEGORIA ==========
def filtrar_por_categoria():
    titulo("🏷️ FILTRAR POR CATEGORIA DE PREÇO", "duplo")
    
    print("Escolha uma categoria:\n")
    print("1. 💎 Premium (acima de R$ 7.000)")
    print("2. ⭐ Alto (R$ 4.500 - R$ 7.000)")
    print("3. 🔵 Médio (R$ 2.500 - R$ 4.500)")
    print("4. 💚 Econômico (abaixo de R$ 2.500)")
    
    try:
        escolha = input("\nEscolha (1-4): ")
        
        categorias = {
            "1": ("💎 Premium", 7000, 999999),
            "2": ("⭐ Alto", 4500, 7000),
            "3": ("🔵 Médio", 2500, 4500),
            "4": ("💚 Econômico", 0, 2500)
        }
        
        if escolha not in categorias:
            print("\n❌ Opção inválida!")
            return
        
        nome_cat, preco_min, preco_max = categorias[escolha]
        
        animacao_carregando(f"Filtrando categoria {nome_cat}", 1)
        
        filtrados = [p for p in todos_celulares if preco_min <= p.preco < preco_max]
        filtrados.sort(key=lambda x: x.custo_beneficio(), reverse=True)
        
        print(f"\n✅ {len(filtrados)} celulares encontrados na categoria {nome_cat}:\n")
        print("─" * 80)
        
        for i, phone in enumerate(filtrados, 1):
            print(f"\n{i}. {phone}")
            print(f"   💰 R$ {phone.preco:,. 2f} | 💎 C/B: {phone.custo_beneficio()} | ⭐ Score: {phone.score_geral()}")
            
    except Exception as e:
        print(f"\n❌ Erro: {e}")


# ========== NOVA: DETALHES DE UM CELULAR ==========
def ver_detalhes_celular():
    titulo("🔍 VER DETALHES COMPLETOS", "duplo")
    
    print("Escolha um celular:\n")
    for i, phone in enumerate(todos_celulares, 1):
        print(f"{i: 2}. {phone} - R$ {phone.preco:,. 2f}")
    
    try:
        escolha = int(input("\nEscolha o celular (número): ")) - 1
        celular = todos_celulares[escolha]
        
        animacao_carregando("Carregando detalhes", 1)
        
        print(celular.detalhes_completos())
        
    except (ValueError, IndexError):
        print("\n❌ Escolha inválida!")


# ========== NOVA:  MELHORES EM CADA CATEGORIA ==========
def melhores_por_categoria():
    titulo("🥇 MELHORES EM CADA CATEGORIA", "duplo")
    
    print("\n🔋 MELHOR BATERIA:")
    melhor_bateria = max(todos_celulares, key=lambda x: x.bateria)
    print(f"   {melhor_bateria} - {melhor_bateria. bateria}mAh")
    barra_progresso(melhor_bateria.bateria, 6000, label="   Capacidade")
    
    print("\n📷 MELHOR CÂMERA:")
    melhor_camera = max(todos_celulares, key=lambda x: x.camera_principal)
    print(f"   {melhor_camera} - {melhor_camera.camera_principal}MP")
    barra_progresso(melhor_camera.camera_principal, 200, label="   Megapixels")
    
    print("\n💾 MAIOR RAM:")
    maior_ram = max(todos_celulares, key=lambda x: x.ram)
    print(f"   {maior_ram} - {maior_ram.ram}GB")
    barra_progresso(maior_ram.ram, 12, label="   Memória")
    
    print("\n📦 MAIOR ARMAZENAMENTO:")
    maior_armazenamento = max(todos_celulares, key=lambda x: x.armazenamento)
    print(f"   {maior_armazenamento} - {maior_armazenamento.armazenamento}GB")
    barra_progresso(maior_armazenamento.armazenamento, 512, label="   Capacidade")
    
    print("\n📱 MAIOR TELA:")
    maior_tela = max(todos_celulares, key=lambda x:  x.tela)
    print(f"   {maior_tela} - {maior_tela.tela}\"")
    barra_progresso(maior_tela.tela, 8, label="   Tamanho")
    
    print("\n💰 MAIS BARATO:")
    mais_barato = min(todos_celulares, key=lambda x: x. preco)
    print(f"   {mais_barato} - R$ {mais_barato.preco:,.2f}")


# ========== RESUMO GERAL ==========
def resumo_geral():
    titulo("📊 RESUMO GERAL", "duplo")
    
    total_vendas_apple = sum(phone.vendas for phone in apple_phones)
    total_vendas_samsung = sum(phone.vendas for phone in samsung_phones)
    total_geral = total_vendas_apple + total_vendas_samsung
    
    preco_medio_apple = sum(p.preco for p in apple_phones) / len(apple_phones)
    preco_medio_samsung = sum(p.preco for p in samsung_phones) / len(samsung_phones)
    
    print(f"📈 ESTATÍSTICAS GERAIS:\n")
    print(f"🍎 Apple: {len(apple_phones)} modelos")
    print(f"   📊 Vendas Totais: {total_vendas_apple: ,} unidades")
    print(f"   💰 Preço Médio: R$ {preco_medio_apple:,.2f}")
    barra_progresso(total_vendas_apple, total_geral, label="   Market Share")
    
    print(f"\n📱 Samsung: {len(samsung_phones)} modelos")
    print(f"   📊 Vendas Totais: {total_vendas_samsung:,} unidades")
    print(f"   💰 Preço Médio: R$ {preco_medio_samsung:,.2f}")
    barra_progresso(total_vendas_samsung, total_geral, label="   Market Share")
    
    print(f"\n{'─' * 80}")
    print(f"📊 TOTAL GERAL: {total_geral:,} unidades vendidas")
    
    if total_vendas_apple > total_vendas_samsung:
        diff = total_vendas_apple - total_vendas_samsung
        print(f"🏆 Líder de Vendas: Apple (+{diff:,} unidades | +{(diff/total_vendas_samsung)*100:.1f}%)")
    else:
        diff = total_vendas_samsung - total_vendas_apple
        print(f"🏆 Líder de Vendas:  Samsung (+{diff:,} unidades | +{(diff/total_vendas_apple)*100:.1f}%)")


# ========== MENU INTERATIVO ==========
def menu_principal():
    while True:
        limpar_tela()
        print("\n")
        print("╔" + "═" * 78 + "╗")
        print("║" + "COMPARADOR DE CELULARES - APPLE VS SAMSUNG 2025". center(78) + "║")
        print("╚" + "═" * 78 + "╝")
        
        print("\n📱 ESCOLHA UMA OPÇÃO:\n")
        print("  1. 🔥 Comparar TOP 3 de Linha")
        print("  2. 🏆 Ver Rankings (TOP 2 de cada)")
        print("  3. ⚔️  Comparação Direta 1 vs 1")
        print("  4. 💰 Buscar por Orçamento")
        print("  5. 🏷️  Filtrar por Categoria de Preço")
        print("  6. 🔍 Ver Detalhes Completos de um Celular")
        print("  7. 🥇 Melhores em Cada Categoria")
        print("  8. 📊 Resumo Geral")
        print("  9. 📋 Ver Todos os Celulares")
        print("  0. 🚪 Sair")
        
        escolha = input("\n➤ Digite sua escolha:  ")
        
        if escolha == "1":
            limpar_tela()
            comparar_top_de_linha()
            pausar()
        elif escolha == "2":
            limpar_tela()
            mostrar_rankings()
            pausar()
        elif escolha == "3":
            limpar_tela()
            comparacao_direta()
            pausar()
        elif escolha == "4":
            limpar_tela()
            buscar_por_orcamento()
            pausar()
        elif escolha == "5": 
            limpar_tela()
            filtrar_por_categoria()
            pausar()
        elif escolha == "6":
            limpar_tela()
            ver_detalhes_celular()
            pausar()
        elif escolha == "7": 
            limpar_tela()
            melhores_por_categoria()
            pausar()
        elif escolha == "8":
            limpar_tela()
            resumo_geral()
            pausar()
        elif escolha == "9":
            limpar_tela()
            titulo("📋 TODOS OS CELULARES", "duplo")
            for i, phone in enumerate(todos_celulares, 1):
                print(f"{i:2}. {phone} - R$ {phone.preco:,.2f} - {phone.categoria_preco()}")
            pausar()
        elif escolha == "0": 
            limpar_tela()
            print("\n✨ Obrigado por usar o Comparador de Celulares! Até logo!  👋\n")
            break
        else:
            print("\n❌ Opção inválida!  Tente novamente.")
            time.sleep(1)


# ========== EXECUTAR PROGRAMA ==========
if __name__ == "__main__":
    menu_principal()

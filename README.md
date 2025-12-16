<div align="center">

# 📱 Comparador de Celulares 2025

### Apple vs Samsung - Análise Completa e Interativa

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

[Características](#-características) • [Instalação](#-instalação) • [Como Usar](#-como-usar) • [Funcionalidades](#-funcionalidades) • [Screenshots](#-screenshots) • [Contribuir](#-contribuir)

---

</div>

## 📖 Sobre o Projeto

O **Comparador de Celulares** é uma aplicação interativa em Python que permite comparar, analisar e encontrar o melhor smartphone entre **5 modelos Apple** e **8 modelos Samsung** lançados em 2025.

Com interface visual atrativa no terminal, rankings inteligentes e múltiplas formas de busca, o sistema ajuda você a tomar a melhor decisão na hora de comprar seu próximo celular!  🎯

---

## ✨ Características

- 🔥 **13 Celulares catalogados** (5 Apple + 8 Samsung)
- 📊 **Análises detalhadas** de especificações técnicas
- 🏆 **Rankings automáticos** por vendas, qualidade e custo-benefício
- ⚔️ **Comparação direta** entre quaisquer dois aparelhos
- 💰 **Busca inteligente** por orçamento
- 🎨 **Interface visual** rica com emojis e bordas estilizadas
- 📈 **Barras de progresso** para comparação visual
- 🔍 **Múltiplos filtros** e categorias de preço

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior instalado
- Terminal/Console com suporte a UTF-8

### Passos para instalação

1. **Clone o repositório** ou baixe o arquivo

```bash
git clone https://github.com/seu-usuario/comparador-celulares.git
cd comparador-celulares
```

2. **Não há dependências externas! ** O projeto usa apenas bibliotecas padrão do Python: 
   - `time`
   - `os`
   - `typing`

3. **Execute o programa**

```bash
python comparador_celulares.py
```

---

## 🎮 Como Usar

### Iniciando o Programa

Execute o script principal:

```bash
python comparador_celulares.py
```

### Menu Principal

Ao iniciar, você verá um menu interativo com 9 opções:

```
╔══════════════════════════════════════════════════════════════════════════════╗
║            COMPARADOR DE CELULARES - APPLE VS SAMSUNG 2025                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

📱 ESCOLHA UMA OPÇÃO: 

  1. 🔥 Comparar TOP 3 de Linha
  2. 🏆 Ver Rankings (TOP 2 de cada)
  3. ⚔️ Comparação Direta 1 vs 1
  4. 💰 Buscar por Orçamento
  5. 🏷️ Filtrar por Categoria de Preço
  6. 🔍 Ver Detalhes Completos de um Celular
  7. 🥇 Melhores em Cada Categoria
  8. 📊 Resumo Geral
  9. 📋 Ver Todos os Celulares
  0. 🚪 Sair
```

### Navegação

- Digite o **número** da opção desejada
- Pressione **ENTER** após cada visualização para voltar ao menu
- Digite **0** para sair do programa

---

## 🎯 Funcionalidades

### 1. 🔥 Comparar TOP 3 de Linha

Exibe os 3 melhores celulares de cada marca com todas as especificações: 
- Processador
- RAM e Armazenamento
- Bateria e Câmera
- Preço e Vendas
- Scores de qualidade e custo-benefício

**Exemplo de saída:**
```
🍎 1º - iPhone 15 Pro Max
├─ 🔧 Processador: A17 Pro
├─ 💾 RAM: 8GB | 📦 Armazenamento: 256GB
├─ 🔋 Bateria: 4422mAh | 📷 Câmera: 48MP
├─ 📱 Tela: 6.7" | 💰 Preço: R$ 7,999.00
├─ 📊 Vendas: 15,000,000 unidades
└─ ⭐ Score: 327. 6 | 💎 C/B: 25.43
```

---

### 2. 🏆 Ver Rankings (TOP 2)

Mostra os **2 melhores** em três categorias diferentes: 

#### 💰 Maiores Vendas
Os celulares mais vendidos do mercado

#### ⭐ Melhores Celulares
Baseado em score técnico geral (RAM, bateria, câmera, tela)

#### 💎 Melhor Custo-Benefício
Relação entre qualidade das especificações e preço

**Exemplo com barra de progresso:**
```
🥇 1º lugar:  Samsung Galaxy A54
   📊 Vendas: 20,000,000 unidades
   💰 Preço:  R$ 2,499.00
   Performance        [████████████████████████████████████████] 100.0%
```

---

### 3. ⚔️ Comparação Direta 1 vs 1

Compare qualquer dois celulares lado a lado! 

**Recursos:**
- Lista todos os 13 celulares disponíveis
- Escolha 2 por número
- Veja comparação detalhada em tabela
- Identificação visual do vencedor em cada categoria

**Exemplo de tabela comparativa:**
```
ESPECIFICAÇÃO         CELULAR 1                CELULAR 2                VENCEDOR  
─────────────────────────────────────────────────────────────────────────────────
💾 RAM                8GB                      12GB                     ✓ C2      
🔋 Bateria            4422mAh                  5000mAh                  ✓ C2      
📷 Câmera             48MP                     200MP                    ✓ C2      
💰 Preço              R$ 7,999.00              R$ 7,499.00              ✓ C2      
```

---

### 4. 💰 Buscar por Orçamento

Encontre o melhor celular dentro do seu budget!

**Como funciona:**
1. Digite seu orçamento máximo (ex: 5000)
2. Sistema busca todos os aparelhos até esse valor
3. Resultados ordenados por **melhor custo-benefício**
4. Veja especificações resumidas de cada opção

**Exemplo:**
```
Digite seu orçamento máximo (R$): 5000

✅ Encontrados 8 celulares dentro do seu orçamento: 

1. Samsung Galaxy A54 - 💚 Econômico
   💰 Preço: R$ 2,499.00
   💎 Custo-Benefício: 48.52
   🔧 8GB RAM, 256GB, 5000mAh, 50MP
```

---

### 5. 🏷️ Filtrar por Categoria de Preço

Os celulares são divididos em 4 categorias:

| Categoria | Faixa de Preço | Emoji |
|-----------|----------------|-------|
| **Premium** | Acima de R$ 7. 000 | 💎 |
| **Alto** | R$ 4.500 - R$ 7.000 | ⭐ |
| **Médio** | R$ 2.500 - R$ 4.500 | 🔵 |
| **Econômico** | Abaixo de R$ 2.500 | 💚 |

Filtre por categoria e veja os melhores de cada faixa!

---

### 6. 🔍 Ver Detalhes Completos

Ficha técnica completa e formatada de qualquer celular: 

```
╔════════════════════════════════════════════════════════════════════════════╗
║  Apple iPhone 15 Pro Max                                                   ║
╠════════════════════════════════════════════════════════════════════════════╣
║  🔧 Processador:        A17 Pro                                             ║
║  💾 RAM:              8GB                                                  ║
║  📦 Armazenamento:    256GB                                                ║
║  🔋 Bateria:          4422mAh                                              ║
║  📷 Câmera:           48MP                                                 ║
║  📱 Tela:             6.7"                                                 ║
║  💰 Preço:             R$ 7,999.00                                          ║
║  📊 Vendas:            15,000,000 unidades                                  ║
║  🏷️ Categoria:        💎 Premium                                           ║
║  ⭐ Score Geral:      327.6                                                ║
║  💎 Custo-Benefício:  25.43                                                ║
╚════════════════════════════════════════════════════════════════════════════╝
```

---

### 7. 🥇 Melhores em Cada Categoria

Descubra os campeões em cada especificação técnica:

- 🔋 **Melhor Bateria**:  Maior capacidade (mAh)
- 📷 **Melhor Câmera**: Maior resolução (MP)
- 💾 **Maior RAM**: Mais memória
- 📦 **Maior Armazenamento**: Mais espaço interno
- 📱 **Maior Tela**: Display maior
- 💰 **Mais Barato**: Menor preço

Com barras de progresso visuais! 

---

### 8. 📊 Resumo Geral

Estatísticas completas do mercado:

- Total de modelos por marca
- Vendas totais e market share
- Preço médio de cada marca
- Líder absoluto de vendas
- Gráficos de participação de mercado

**Exemplo:**
```
📈 ESTATÍSTICAS GERAIS: 

🍎 Apple:  5 modelos
   📊 Vendas Totais: 58,000,000 unidades
   💰 Preço Médio: R$ 5,599.20
   Market Share       [████████████████████████░░░░░░░░░░░░░░░░] 61.7%

📱 Samsung: 8 modelos
   📊 Vendas Totais: 93,000,000 unidades
   💰 Preço Médio: R$ 4,899.25
   Market Share       [██████████████████████████████████████░░] 38.3%

🏆 Líder de Vendas: Samsung (+35,000,000 unidades | +60. 3%)
```

---

### 9. 📋 Ver Todos os Celulares

Lista completa e numerada de todos os 13 celulares com: 
- Marca e modelo
- Preço
- Categoria de preço

---

## 📱 Celulares Incluídos

### 🍎 **Apple (5 modelos)**

| Modelo | Processador | RAM | Armazenamento | Preço |
|--------|-------------|-----|---------------|-------|
| iPhone 15 Pro Max | A17 Pro | 8GB | 256GB | R$ 7.999 |
| iPhone 15 Pro | A17 Pro | 8GB | 256GB | R$ 6.999 |
| iPhone 15 Plus | A16 Bionic | 6GB | 128GB | R$ 5.999 |
| iPhone 15 | A16 Bionic | 6GB | 128GB | R$ 4.999 |
| iPhone SE (2025) | A15 Bionic | 4GB | 64GB | R$ 2.999 |

### 📱 **Samsung (8 modelos)**

| Modelo | Processador | RAM | Armazenamento | Preço |
|--------|-------------|-----|---------------|-------|
| Galaxy S24 Ultra | Snapdragon 8 Gen 3 | 12GB | 512GB | R$ 7.499 |
| Galaxy S24+ | Snapdragon 8 Gen 3 | 12GB | 256GB | R$ 5.999 |
| Galaxy S24 | Snapdragon 8 Gen 3 | 8GB | 256GB | R$ 4.999 |
| Galaxy Z Fold 5 | Snapdragon 8 Gen 2 | 12GB | 512GB | R$ 9.999 |
| Galaxy Z Flip 5 | Snapdragon 8 Gen 2 | 8GB | 256GB | R$ 5.499 |
| Galaxy A54 | Exynos 1380 | 8GB | 256GB | R$ 2.499 |
| Galaxy A34 | Dimensity 1080 | 6GB | 128GB | R$ 1.799 |
| Galaxy M54 | Exynos 1380 | 8GB | 256GB | R$ 2.199 |

---

## 🧮 Sistema de Pontuação

### Score Geral
Avalia a qualidade técnica do aparelho:

```python
Score = (RAM × 10) + (Armazenamento ÷ 10) + (Bateria ÷ 10) + 
        (Câmera ÷ 2) + (Tela × 15)
```

### Score de Custo-Benefício
Relaciona especificações com o preço:

```python
Custo-Benefício = [(RAM + Armazenamento/10 + Bateria/100 + 
                    Câmera/10 + Tela) ÷ Preço] × 10000
```

**Quanto maior o score, melhor o aparelho!**

---

## 🎨 Screenshots

### Menu Principal
```
╔══════════════════════════════════════════════════════════════════════════════╗
║            COMPARADOR DE CELULARES - APPLE VS SAMSUNG 2025                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### Comparação TOP 3
```
🔥 COMPARAÇÃO - TOP DE LINHA (3 de cada marca)
═══════════════════════════════════════════════════════════════════════════════

📱 APPLE - TOP 3:
────────────────────────────────────────────────────────────────────────────────

🍎 1º - iPhone 15 Pro Max
├─ 🔧 Processador: A17 Pro
├─ 💾 RAM: 8GB | 📦 Armazenamento: 256GB
└─ ⭐ Score: 327.6 | 💎 C/B: 25.43
```

### Rankings com Barras de Progresso
```
💰 TOP 2 - MAIORES VENDAS
────────────────────────────────────────────────────────────────────────────────

🥇 1º lugar:  Samsung Galaxy A54 - 20,000,000 unidades vendidas
   Performance        [████████████████████████████████████████] 100.0%
```

### Animação de Carregamento
```
Carregando detalhes ⠋
```

---

## 🛠️ Estrutura do Código

### Classe Principal

```python
class Celular:
    """Representa um smartphone com todas as suas especificações"""
    
    # Atributos
    - marca, modelo, processador
    - ram, armazenamento, bateria
    - camera_principal, tela, preco, vendas
    - is_top_linha
    
    # Métodos
    - custo_beneficio()    # Calcula score C/B
    - score_geral()        # Calcula score técnico
    - score_bateria()      # Score de bateria
    - score_camera()       # Score de câmera
    - categoria_preco()    # Retorna categoria
    - detalhes_completos() # Ficha técnica formatada
```

### Funções Principais

| Função | Descrição |
|--------|-----------|
| `comparar_top_de_linha()` | Compara os 3 top de cada marca |
| `mostrar_rankings()` | Exibe TOP 2 de cada categoria |
| `comparacao_direta()` | Compara 2 celulares escolhidos |
| `buscar_por_orcamento()` | Busca por faixa de preço |
| `filtrar_por_categoria()` | Filtra por categoria |
| `ver_detalhes_celular()` | Mostra ficha completa |
| `melhores_por_categoria()` | Campeões em cada spec |
| `resumo_geral()` | Estatísticas do mercado |
| `menu_principal()` | Menu interativo |

### Funções Utilitárias

| Função | Descrição |
|--------|-----------|
| `limpar_tela()` | Limpa o console |
| `pausar()` | Aguarda ENTER |
| `animacao_carregando()` | Exibe loading animado |
| `titulo()` | Cria títulos estilizados |
| `barra_progresso()` | Desenha barra visual |

---

## 💡 Exemplos de Uso

### Exemplo 1: Encontrar o melhor custo-benefício

```bash
➤ Digite sua escolha:  2

💎 TOP 2 - MELHOR CUSTO-BENEFÍCIO
────────────────────────────────────────────────────────────────

🥇 1º lugar:  Samsung Galaxy M54
   💎 Score C/B: 52.89
   💰 Preço: R$ 2,199.00
   🔧 Specs: 8GB RAM, 256GB, 108MP
```

### Exemplo 2: Comparar iPhone vs Samsung

```bash
➤ Digite sua escolha: 3

Escolha o primeiro celular (número): 1
Escolha o segundo celular (número): 6

⚔️ Apple iPhone 15 Pro Max VS Samsung Galaxy S24 Ultra

VENCEDOR GERAL:  Samsung Galaxy S24 Ultra (6 categorias)
```

### Exemplo 3: Buscar por orçamento de R$ 3.000

```bash
➤ Digite sua escolha: 4

Digite seu orçamento máximo (R$): 3000

✅ Encontrados 4 celulares dentro do seu orçamento

1. Samsung Galaxy M54 - 💚 Econômico
   💎 Custo-Benefício: 52.89
```

---

## 🤝 Contribuir

Contribuições são muito bem-vindas! 🎉

### Como contribuir:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um **Pull Request**

### Ideias de melhorias:

- [ ] Adicionar mais marcas (Xiaomi, Motorola, etc)
- [ ] Salvar comparações em arquivo
- [ ] Gráficos com matplotlib
- [ ] Interface gráfica (Tkinter/PyQt)
- [ ] Exportar relatórios em PDF
- [ ] Sistema de favoritos
- [ ] Histórico de preços
- [ ] Integração com APIs de preços reais
- [ ] Modo escuro/claro
- [ ] Suporte a múltiplos idiomas

---

## 📝 Licença

Este projeto está sob a licença MIT.  Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

```
MIT License

Copyright (c) 2025 Comparador de Celulares

Permission is hereby granted, free of charge, to any person obtaining a copy... 
```

---

## 👨‍💻 Autor

Desenvolvido com ❤️ e ☕ por **[Seu Nome]**

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [Seu Nome](https://linkedin.com/in/seu-perfil)
- Email: seu. email@exemplo.com

---

## 📞 Suporte

Encontrou um bug?  Tem alguma sugestão? 

- 🐛 [Reportar Bug](https://github.com/seu-usuario/comparador-celulares/issues)
- 💡 [Sugerir Feature](https://github.com/seu-usuario/comparador-celulares/issues)
- 📧 [Contato Direto](mailto:seu.email@exemplo.com)

---

## 🙏 Agradecimentos

- Comunidade Python 🐍
- Todos os contribuidores 👥
- Você por usar este projeto!  ⭐

---

## 📊 Status do Projeto

![GitHub repo size](https://img.shields.io/github/repo-size/seu-usuario/comparador-celulares?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/seu-usuario/comparador-celulares? style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/seu-usuario/comparador-celulares?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/seu-usuario/comparador-celulares? style=flat-square)

---

<div align="center">

### ⭐ Se este projeto foi útil, deixe uma estrela! ⭐

**Feito com 💙 em Python**

[⬆ Voltar ao topo](#-comparador-de-celulares-2025)

</div>

# 📱 Comparador de Celulares - Apple vs Samsung 2025

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB? style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green. svg? style=for-the-badge)](LICENSE)

> **Aplicação web interativa para comparar especificações, preços e custo-benefício de celulares Apple e Samsung de 2025.**

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Demonstração](#-demonstração)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Celulares Disponíveis](#-celulares-disponíveis)
- [Métricas de Avaliação](#-métricas-de-avaliação)
- [Capturas de Tela](#-capturas-de-tela)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 🎯 Sobre o Projeto

O **Comparador de Celulares** é uma aplicação web desenvolvida com **Streamlit** que permite comparar de forma visual e interativa os principais smartphones de 2025 das marcas **Apple** e **Samsung**. 

### 💡 Motivação

Com tantos modelos no mercado, escolher o celular ideal pode ser desafiador. Este projeto foi criado para: 

- ✅ Facilitar a comparação entre diferentes modelos
- ✅ Calcular automaticamente o custo-benefício
- ✅ Visualizar rankings de forma clara
- ✅ Ajudar na tomada de decisão de compra

### 🎓 Contexto

Este projeto foi originalmente desenvolvido para rodar no **LEGO SPIKE Prime** (robô educacional) e depois adaptado para uma aplicação web moderna usando **Streamlit**. 

---

## 🎬 Demonstração

![Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=Comparador+de+Celulares)

### 🚀 Como Executar

```bash
streamlit run comparador_celulares.py
```

---

## ⚡ Funcionalidades

### 🔥 Comparar TOP 3
- Visualize os 3 melhores modelos de cada marca
- Especificações completas (RAM, bateria, câmera, etc.)
- Scores de avaliação e custo-benefício

### 🏆 Ver Rankings
- **TOP 2 - Melhor Score Geral**:  Celulares com melhor desempenho técnico
- **TOP 2 - Melhor Custo-Benefício**: Melhores relações qualidade/preço

### ⚔️ Comparação 1 vs 1
- Compare **iPhone 15 Pro Max** vs **Galaxy S24 Ultra**
- Comparação lado a lado de todas as especificações
- Declaração automática do vencedor

### 📋 Todos os Celulares
- Lista completa dos 6 modelos cadastrados
- Visualização detalhada de cada especificação
- Preços atualizados para 2025

### 🥇 Melhores Specs
- **Maior RAM**:  Qual celular tem mais memória
- **Maior Armazenamento**:  Maior capacidade de dados
- **Melhor Bateria**: Maior duração
- **Melhor Câmera**: Mais megapixels
- **Mais Barato**: Melhor preço

### 📊 Resumo Geral
- Score médio de cada marca
- Comparação Apple vs Samsung
- Declaração da marca vencedora

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white) | 3.8+ | Linguagem principal |
| ![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?logo=streamlit&logoColor=white) | 1.28+ | Framework web |

### 📦 Dependências

```txt
streamlit>=1.28.0
```

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**

```bash
git clone https://github.com/bimadevfullComparador/Apple-vs-Samsung-2025.git
cd Apple-vs-Samsung-2025
```

2. **Crie um ambiente virtual (opcional, mas recomendado)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install streamlit
```

4. **Execute a aplicação**

```bash
streamlit run comparador_celulares. py
```

5. **Abra no navegador**

A aplicação abrirá automaticamente em:  **http://localhost:8501**

---

## 💻 Como Usar

### Interface Principal

1. **Sidebar (Menu Lateral)**
   - Use o menu dropdown para navegar entre as seções
   - 6 opções disponíveis

2. **Área Principal**
   - Visualize os dados de acordo com a opção selecionada
   - Interaja com as comparações

### Navegação

```
📱 Comparador de Celulares
│
├── 🔥 Comparar TOP 3        → Mostra os 3 melhores de cada marca
├── 🏆 Ver Rankings          → TOP 2 em diferentes categorias
├── ⚔️ Comparação 1 vs 1     → iPhone 15 Pro Max vs Galaxy S24 Ultra
├── 📋 Todos os Celulares    → Lista completa com detalhes
├── 🥇 Melhores Specs        → Campeões em cada especificação
└── 📊 Resumo Geral          → Comparação entre marcas
```

---

## 📁 Estrutura do Projeto

```
Apple-vs-Samsung-2025/
│
├── comparador_celulares.py    # Código principal (Streamlit)
├── README.md                   # Documentação (este arquivo)
├── requirements.txt            # Dependências
├── LICENSE                     # Licença MIT
│
├── . gitignore                  # Arquivos ignorados pelo Git
└── assets/                     # Imagens e recursos
    └── screenshots/            # Capturas de tela
```

---

## 📱 Celulares Disponíveis

### 🍎 Apple (3 modelos)

| Modelo | RAM | Armazenamento | Bateria | Câmera | Preço |
|--------|-----|---------------|---------|--------|-------|
| **iPhone 15 Pro Max** | 8GB | 256GB | 4422mAh | 48MP | R$ 7.999,00 |
| **iPhone 15** | 6GB | 128GB | 3349mAh | 48MP | R$ 4.999,00 |
| **iPhone SE (2025)** | 4GB | 64GB | 2018mAh | 12MP | R$ 2.999,00 |

### 📱 Samsung (3 modelos)

| Modelo | RAM | Armazenamento | Bateria | Câmera | Preço |
|--------|-----|---------------|---------|--------|-------|
| **Galaxy S24 Ultra** | 12GB | 512GB | 5000mAh | 200MP | R$ 7.499,00 |
| **Galaxy S24** | 8GB | 256GB | 4000mAh | 50MP | R$ 4.999,00 |
| **Galaxy A54** | 8GB | 256GB | 5000mAh | 50MP | R$ 2.499,00 |

---

## 📊 Métricas de Avaliação

### 🎯 Score Geral

Avalia o desempenho técnico do celular com base nas especificações:

```python
Score Geral = (RAM × 10) + (Armazenamento ÷ 10) + (Bateria ÷ 10) + (Câmera ÷ 2)
```

**Exemplo:**
- iPhone 15 Pro Max: `(8×10) + (256÷10) + (4422÷10) + (48÷2) = 567,8`

### 💎 Custo-Benefício

Relaciona as especificações com o preço: 

```python
C/B = [(RAM + Armazenamento/10 + Bateria/100 + Câmera/10) / Preço] × 10000
```

**Quanto maior, melhor o custo-benefício!**

**Exemplo:**
- Galaxy A54: `[(8 + 25. 6 + 50 + 5) / 2499] × 10000 = 35,45` ⭐

---

## 📸 Capturas de Tela

### Tela Inicial
![Home](https://via.placeholder.com/800x400/667eea/ffffff?text=Tela+Inicial)

### Comparação TOP 3
![TOP3](https://via.placeholder.com/800x400/764ba2/ffffff?text=TOP+3+de+Linha)

### Rankings
![Rankings](https://via.placeholder.com/800x400/f5576c/ffffff?text=Rankings)

### Comparação 1x1
![1x1](https://via.placeholder.com/800x400/667eea/ffffff?text=Comparação+1x1)

---

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! 

### Como Contribuir

1. **Fork o projeto**
2. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/MinhaNovaFuncionalidade
   ```
3. **Commit suas mudanças**
   ```bash
   git commit -m 'Adiciona nova funcionalidade X'
   ```
4. **Push para a branch**
   ```bash
   git push origin feature/MinhaNovaFuncionalidade
   ```
5. **Abra um Pull Request**

### Ideias para Contribuição

- [ ] Adicionar mais modelos de celulares
- [ ] Incluir outras marcas (Xiaomi, Motorola, etc.)
- [ ] Criar gráficos comparativos com Plotly
- [ ] Adicionar filtros de busca avançada
- [ ] Implementar tema escuro/claro
- [ ] Adicionar exportação de dados em PDF
- [ ] Criar API REST

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

```
MIT License

Copyright (c) 2025 bimadevfullComparador

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Contato

**bimadevfullComparador**

- 🐙 GitHub: [@bimadevfullComparador](https://github.com/bimadevfullComparador)
- 📧 Email: contato@exemplo.com
- 💼 LinkedIn: [seu-perfil](https://linkedin.com/in/seu-perfil)

---

## 🎓 Aprendizados

Este projeto foi desenvolvido para demonstrar:

- ✅ Programação Orientada a Objetos em Python
- ✅ Desenvolvimento de interfaces com Streamlit
- ✅ Manipulação de dados e listas
- ✅ Cálculos de métricas personalizadas
- ✅ Boas práticas de código e documentação

---

## 🔮 Roadmap

- [x] Versão básica com 6 celulares
- [x] Interface Streamlit
- [x] Sistema de comparação
- [ ] Adicionar gráficos interativos
- [ ] Incluir 20+ modelos
- [ ] Sistema de favoritos
- [ ] Compartilhamento de comparações
- [ ] Deploy em nuvem (Streamlit Cloud)
- [ ] Versão mobile (PWA)

---

## ⭐ Mostre seu apoio

Se este projeto foi útil para você, considere dar uma ⭐! 

[![Star](https://img.shields.io/github/stars/bimadevfullComparador/Apple-vs-Samsung-2025?style=social)](https://github.com/bimadevfullComparador/Apple-vs-Samsung-2025)

---

## 🙏 Agradecimentos

- [Streamlit](https://streamlit.io/) - Framework incrível para criar apps web em Python
- [Python](https://www.python.org/) - Linguagem de programação
- Comunidade open source 💜

---

<div align="center">

**Feito com ❤️ e Python**

[⬆ Voltar ao topo](#-comparador-de-celulares---apple-vs-samsung-2025)

</div>

---

## 📝 Notas da Versão

### v1.0.0 (2025-12-16)

#### ✨ Novidades
- Interface inicial com Streamlit
- 6 modelos de celulares (3 Apple + 3 Samsung)
- Sistema de comparação completo
- Cálculo de custo-benefício
- Rankings TOP 2

#### 🐛 Correções
- Primeira versão estável

#### 📚 Documentação
- README completo
- Comentários no código
- Guia de instalação

---

**💡 Dica:** Para atualizar a aplicação, basta fazer `git pull` e reiniciar o Streamlit! 

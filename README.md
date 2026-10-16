# Learning Python 🐍

Repositório dedicado ao estudo prático de fundamentos da linguagem, estruturas de dados e arquitetura de software orientada a objetos (**POO**).

---

## 🏆 Top 5 Projetos em Destaque

Aqui estão os 5 projetos de maior maturidade arquitetural e lógica do repositório:

### 1. ⚔️ Sertão Roguelike 2.0 (`rpg_poo.py`)
> **O auge da arquitetura Orientada a Objetos.**  
* **Herança & `super()`:** Classe base `Personagem` herdada por `Guerreiro`, `Mago`, `Arqueiro` e `Monstro`, eliminando duplicação de código.
* **Polimorfismo:** Método `usar_especial()` padronizado em todas as classes, permitindo um motor de combate unificado que descobre a habilidade certa de cada herói em tempo de execução.
* **Gestão de Recursos:** Controle de `mana` para o Mago e limite de vigor/usos para o Guerreiro.
* **Geração Dinâmica:** Instanciação em tempo real de monstros com atributos sorteados.

### 2. 🏜️ Sertão Roguelike 1.0 (`rpg.py`)
> **Jogo roguelike procedural completo no terminal.**  
* Exploração com encontros aleatórios, loja de consumíveis e mochila dinâmica (`list.pop()`).
* Travas matemáticas `min()` e `max()` para evitar vidas estouradas ou números negativos em combate.
* Tratamento de exceções com `.isdigit()` impedindo encerramento abrupto por erros de digitação.

### 3. 🏦 Sistema Bancário (`banco.py` & `banco_teste.py`)
> **Simulador de operações financeiras e regras de negócio.**  
* Fluxo completo de depósito, saque e consulta de extrato.
* Encapsulamento de saldo e validação de operações contra saques impossíveis.
* Suíte de testes lógicos para validação de integridade financeira.

### 4. 🛒 Gestão Comercial & Estoque (`gerenciamento_produtos.py` & `loja.py`)
> **Controle de catálogo e fluxo de caixa de vendas.**  
* Estruturação de dados com listas de dicionários representando inventários.
* Atualização de quantidades, precificação e cálculo automático de saldo e faturamento.

### 5. 🔐 Criptografia & Segurança (`criptografia.py` & `forca_senha.py`)
> **Ofuscação de mensagens e análise de credenciais.**  
* Implementação de cifra para embaralhamento e decodificação de mensagens.
* Validador de complexidade de senhas através de análise estrita de caracteres (maiúsculas, minúsculas, números e símbolos).

---

## 📂 Outros Exercícios de Fixação

Além dos projetos principais, o repositório conta com exercícios focados em fundamentos de lógica e manipulação de dados:

* **Cálculos & Finanças:** `calculadora_gastos.py`, `calculo_lucro.py`, `calculo_vendas_bonus.py`, `carrinho_compras.py`.
* **Saúde & Utilitários:** `calculadora_imc.py`, `dados.py`, `senha.py`.
* **Gestão & Produtividade:** `gerenciador_contatos.py`, `sistema_agenda.py`, `sistema_notas.py`.

---

## 🛠️ Como Executar

1. **Pré-requisitos:** Ter o [Python 3.10+](https://www.python.org/) instalado.
2. **Clonar o repositório:**
   ```bash
   git clone https://github.com/FelipeJesus83/learning-python.git
   cd learning-python
   ```
3. **Executar qualquer projeto:**
   ```bash
   python rpg_poo.py
   ```

---

## 👤 Autor

* **Felipe Jesus**  
* GitHub: [@FelipeJesus83](https://github.com/FelipeJesus83)

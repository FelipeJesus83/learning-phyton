# Learning Python 🐍

Repositório dedicado ao estudo prático de fundamentos da linguagem, estruturas de dados e arquitetura de software orientada a objetos (**POO**).

---

## 🏆 Top 5 Projetos em Destaque

Aqui estão os 5 projetos de maior maturidade arquitetural e lógica do repositório:

### 1. 🏦 Sistema Bancário & Gestão de Contas (`sistema_bancario.py`)
> **O projeto mais avançado e completo em Arquitetura Orientada a Objetos (POO).**  
* **Composição & Agregação:** Relação estrita onde `Pessoa` é composta por `Endereco`, e `Conta` associa e gerencia uma instância completa de `Pessoa`.
* **Herança Multinível:** Cadeia de herança com especialização de cargos (`Pessoa` -> `Funcionario` -> `Gerente`) com reaproveitamento via `super().__init__()`.
* **Polimorfismo Real:** Sobrescrita de métodos onde `ContaCorrente` implementa saque com taxa bancária e limite de cheque especial (saldo negativo permitido), enquanto `ContaPoupanca` implementa controle estrito de saldo e cálculo de rendimento de juros (`render_jrs`).
* **Verificação de Tipos Dinâmica:** Uso de `isinstance()` para validação em tempo de execução de operações restritas por tipo de conta.
* **Interface CLI Profissional:** Sistema interativo completo no terminal com cadastro guiado, onboarding e menu transacional dinâmico.

### 2. ⚔️ Sertão Roguelike 2.0 (`rpg_poo.py`)
> **RPG tático baseado em classes e herança.**  
* **Herança & `super()`:** Classe base `Personagem` herdada por `Guerreiro`, `Mago`, `Arqueiro` e `Monstro`, eliminando duplicação de código.
* **Polimorfismo em Combate:** Método `usar_especial()` padronizado em todas as classes, permitindo um motor de combate unificado que descobre a habilidade certa de cada herói em tempo de execução.
* **Gestão de Recursos:** Controle de `mana` para o Mago e limite de vigor/usos para o Guerreiro.
* **Geração Dinâmica:** Instanciação em tempo real de monstros com atributos sorteados.

### 3. 🛒 Simulador de E-commerce (`carrinho.py`)
> **Sistema de carrinho de compras e checkout.**  
* **Agregação:** Classe `Carrinho` gerenciando uma coleção dinâmica de objetos `Produto`.
* **Regras de Negócio:** Cálculo de subtotal, aplicação condicional de descontos e remoção segura de itens por busca interna.
* **Menu Interativo:** Interface CLI com loop de eventos para adição, exclusão e cálculo de pedidos.

### 4. 🏜️ Sertão Roguelike 1.0 (`rpg.py`)
> **Jogo roguelike procedural completo no terminal.**  
* Exploração com encontros aleatórios, loja de consumíveis e mochila dinâmica (`list.pop()`).
* Travas matemáticas `min()` e `max()` para evitar vidas estouradas ou números negativos em combate.
* Tratamento de exceções com `.isdigit()` impedindo encerramento abrupto por erros de digitação.

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
3. **Executar o Sistema Bancário:**
   ```bash
   python sistema_bancario.py
   ```

---

## 👤 Autor

* **Felipe Jesus**  
* GitHub: [@FelipeJesus83](https://github.com/FelipeJesus83)

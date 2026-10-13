# Learning Python 🐍

Repositório dedicado ao estudo prático e contínuo de fundamentos de programação e resolução de problemas utilizando **Python**.

---

## 🚀 Projeto em Destaque

### 🎮 Sertão Roguelike RPG (`rpg.py`)
Jogo em modo texto desenvolvido no terminal explorando mecânicas completas de RPG:
* **Gerenciamento de Estado**: Vida, vida máxima, ataque, inventário dinâmico e saldo de ouro.
* **Sistema de Combate por Turnos**: Controle matemático de dano com travas de limite (`min` / `max`) evitando valores negativos ou vidas estouradas.
* **Economia e Inventário**: Loja com itens consumíveis clonados por valor (`.copy()`), evitando corrupção de estado por referência na memória.
* **Mochila Dinâmica**: Consumo e remoção de itens em tempo de execução via `list.pop()`.
* **Tratamento de Entradas**: Validação com `.isdigit()` impedindo encerramento abrupto (`ValueError`).

```bash
# Como executar o RPG:
python rpg.py
```

---

## 📂 Projetos e Exercícios de Fixação

| Arquivo | Descrição | Conceitos Aplicados |
| :--- | :--- | :--- |
| `rpg.py` | RPG roguelike por turnos com combate, loja e mochila | Loops, Dicionários, Clonagem de Memória, Validações |
| `banco.py` | Sistema bancário com depósito, saque e extrato | Condicionais, Formatação numérica, Controle de saldo |
| `banco_teste.py` | Testes de operações e regras de negócio bancárias | Validação lógica e cenários de teste |
| `calculadora_gastos.py` | Controle financeiro simples de despesas | Operações matemáticas, Acumuladores |
| `calculadora_imc.py` | Classificação de índice de massa corporal | Condicionais encadeadas (`if/elif/else`) |
| `calculo_lucro.py` | Análise de receita, custos e margem líquida | Operadores aritméticos, Regras financeiras |
| `calculo_vendas_bonus.py` | Bonificação por meta atingida | Lógica condicional e cálculo percentual |
| `carrinho_compras.py` | Simulação de checkout e soma de itens | Listas, Iteração (`for`), totalização |
| `criptografia.py` | Cifra e ofuscação básica de mensagens | Manipulação de strings, laços |
| `dados.py` | Tratamento e estruturação de dados tabulares/listas | Estruturas de dados básicas |
| `gerenciador_contatos.py` | Agenda com busca e cadastro de contatos | Dicionários, Chave-valor |
| `gerenciamento_produtos.py` | Controle de estoque e catálogo | Listas de dicionários, Atualização de dados |
| `loja.py` | Sistema de compras e fluxo de caixa de loja | Menus iterativos, Entrada de usuário |
| `senha.py` | Validador e gerador de requisitos de senha | Manipulação de caracteres, Checagem de complexidade |
| `sistema_agenda.py` | Agendamento e gerenciamento de compromissos | Listas, Filtros, Busca |
| `sistema_notas.py` | Cálculo de médias escolares e aprovação | Funções embutidas, Listas, Médias |

---

## 🛠️ Como Executar

1. **Pré-requisitos**: Ter o [Python 3.10+](https://www.python.org/) instalado.
2. **Clonar o repositório**:
   ```bash
   git clone https://github.com/FelipeJesus83/Learning.phyton.git
   cd Learning.phyton
   ```
3. **Executar qualquer script**:
   ```bash
   python nome_do_arquivo.py
   ```

---

## 👤 Autor

* **Felipe Jesus**  
* GitHub: [@FelipeJesus83](https://github.com/FelipeJesus83)

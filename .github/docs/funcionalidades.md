# FUNCIONALIDADES

1. Funcionalidades Essenciais
  Estas são as ações que seu sistema permitirá ao usuário:

    - Autenticação e Autorização:
      - [ ] **Cadastro de Usuário**: Permitir que novos usuários criem contas.
      - [ ] **Login de Usuário**: Permitir que usuários existentes façam login e obtenham um token de acesso (JWT é uma boa escolha).
      - [ ] **Proteção de Rotas:**: Garantir que apenas usuários autenticados e autorizados possam acessar certas funcionalidades.
    
    - Gestão de Transações:
      - [ ] **Registrar Receita**:  Adicionar uma nova entrada de dinheiro (salário, bônus, etc.) com valor, data, descrição e categoria.
      - [ ] **Registrar Despesa**: Adicionar uma nova saída de dinheiro (aluguel, alimentação, transporte, etc.) com valor, data, descrição, categoria e forma de pagamento.
      - [ ] **Listar Transações**: Exibir todas as transações de um usuário, com opções de filtro (por data, categoria, tipo, etc.).
      - [ ] **Visualizar Detalhes da Transação**: Exibir informações detalhadas de uma transação específica.
      - [ ] **Atualizar Transação**: Modificar os detalhes de uma transação existente.
      - [ ] **Excluir Transação**: Remover uma transação.
    
    - Gestão de Categorias:
      - [ ] **Cadastrar Categoria**: Adicionar novas categorias (ex: "Moradia", "Transporte", "Lazer").
      - [ ] **Listar Categorias**: Exibir todas as categorias disponíveis para o usuário.
      - [ ] **Visualizar Detalhes da Categoria**: Exibir informações detalhadas de uma categoria específica.
      - [ ] **Atualizar Categoria**: Modificar o nome ou descrição de uma categoria.
      - [ ] **Excluir Categoria**: Remover uma categoria (com tratamento para transações associadas).

    - Orçamento:
      - [ ] **Definir Orçamento Mensal**: Definir um orçamento mensal para o usuário.
      - [ ] **Visualizar Orçamento Mensal**: Exibir o orçamento mensal atual e suas transações associadas.
      - [ ] **Atualizar Orçamento Mensal**: Modificar o orçamento mensal.
      - [ ] **Definir Orçamento por Categoria:**: Permitir que o usuário defina um limite de gastos para uma categoria específica em um período (ex: R$500 para Alimentação em junho).
      - [ ] **Acompanhar Orçamento**: Mostrar o quanto já foi gasto em relação ao orçamento definido para cada categoria.

    - Relatórios e Análises:
      - [ ] **Saldo Atual**: Calcular e exibir o saldo total do usuário.
      - [ ] **Extrato por Período**: Gerar um extrato detalhado de receitas e despesas em um determinado período.
      - [ ] **Gastos por Categoria**: Apresentar uma quebra dos gastos por categoria (pode ser visualizado com gráficos).
      - [ ] **Comparativo de Períodos**: Comparar receitas/despesas entre diferentes meses ou anos.

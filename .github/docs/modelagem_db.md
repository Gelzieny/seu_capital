# MODELAGEM DE DADOS
Modelagem de Dados para Controle Financeiro

Abaixo as entidades (tabelas) e seus atributos (colunas), incluindo os tipos de dados e os relacionamentos.

  1. Usuário (`User`):
  Esta entidade armazena as informações básicas de cada pessoa que usará o sistema.

  - `id`: (Chave Primária, Inteiro) Identificador único do usuário. Auto-incrementável.
  - `username`: (String, Único) Nome de usuário escolhido. Ex: "joao.silva".
  - `email`: (String, Único) Endereço de e-mail do usuário. Usado para login e recuperação de senha.
  - `hashed_password`: (String) Senha do usuário criptografada (hash). Nunca armazene senhas em texto puro!
  - `created_at`: (Datetime) Data e hora de criação da conta do usuário.
  - `updated_at`: (Datetime) Última data e hora de atualização das informações do usuário.

  2. Categoria (`Category`)
  
  As categorias organizam as transações, como "Alimentação", "Transporte", "Salário", etc. Podem ser padronizadas ou criadas pelo usuário.

  - `id`: (Chave Primária, Inteiro) Identificador único da categoria. Auto-incrementável.
  - `user_id`: (Chave Estrangeira, Inteiro) Referencia o id do User ao qual esta categoria pertence. Permite categorias personalizadas por usuário. Pode ser Nulo se a categoria for padrão do sistema.
  - `name`: (String) Nome da categoria. Ex: "Aluguel", "Salário", "Lazer".
  - `type`: (String) Tipo da categoria. Valores possíveis: "receita" ou "despesa".
  - `description`: (String, Opcional) Uma breve descrição da categoria.
  - `is_default`: (Booleano) Indica se é uma categoria padrão do sistema (True) ou criada pelo usuário (False).
  - `created_at`: (Datetime) Data e hora de criação da categoria.
  - `updated_at`: (Datetime) Última data e hora de atualização da categoria.

  3. Transação (`Transaction`)
  Esta é a entidade central que registra cada movimentação financeira.

  - `id`: (Chave Primária, Inteiro) Identificador único da transação. Auto-incrementável.
  - `user_id`: (Chave Estrangeira, Inteiro) Referencia o id do User que realizou a transação. (Obrigatório)
  - `category_id`: (Chave Estrangeira, Inteiro) Referencia o id da Category à qual a transação pertence. (Obrigatório)
  - `amount`: (Decimal/Float) O valor da transação. Use Decimal para maior precisão em valores monetários. (Obrigatório)
  - `type`: (String) Indica se é uma "receita" ou "despesa". (Obrigatório)
  - `date`: (Date) A data em que a transação ocorreu. (Obrigatório)
  - `description`: (String, Opcional) Uma descrição detalhada da transação.
  - `payment_method`: (String, Opcional) Como a transação foi paga/recebida. Ex: "Cartão de Crédito", "Dinheiro", "Pix", "Transferência Bancária".
  - `created_at`: (Datetime) Data e hora de registro da transação no sistema.
  - `updated_at`: (Datetime) Última data e hora de atualização da transação.

  4. Orçamento (`Budget`)
  Permite que os usuários definam limites de gastos para categorias em períodos específicos.

  - `id`: (Chave Primária, Inteiro) Identificador único do orçamento. Auto-incrementável.
  - `user_id`: (Chave Estrangeira, Inteiro) Referencia o id do User que definiu o orçamento. (Obrigatório)
  - `category_id`: (Chave Estrangeira, Inteiro) Referencia o id da Category à qual este orçamento se aplica. (Obrigatório)
  - `amount_limit`: (Decimal/Float) O valor máximo permitido para gastar nesta categoria no período. (Obrigatório)
  - `start_date`: (Date) Data de início do período do orçamento (ex: primeiro dia do mês). (Obrigatório)
  - `end_date`: (Date) Data de fim do período do orçamento (ex: último dia do mês). (Obrigatório)
  - `created_at`: (Datetime) Data e hora de criação do orçamento.
  - `updated_at`: (Datetime) Última data e hora de atualização do orçamento.
  
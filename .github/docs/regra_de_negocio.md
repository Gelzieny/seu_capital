# REGRAS DE NEGÓCIO

Estas são as regras que governam o comportamento do sistema financeiro:

  - [ ] **Saldo do Usuário**: O saldo total é a soma de todas as receitas menos a soma de todas as despesas.

  - **Transações Negativas**:
    - [ ] Receitas não podem ter valor negativo.
    - [ ] Despesas não podem ter valor negativo.

  - **Consistência de Dados**:
    - [ ] Uma transação deve sempre ser associada a um usuário.
    - [ ] Uma transação deve sempre ser associada a uma categoria (ou uma categoria padrão se nenhuma for especificada).
    - [ ] Não é permitido excluir uma categoria se houver transações vinculadas a ela (ou as transações devem ser reassociadas a uma categoria padrão/genérica).

  - **Orçamento**:
    - O orçamento é por usuário e por categoria e período (mês/ano).
    - Quando uma despesa é registrada, ela deve ser contabilizada no orçamento da categoria correspondente.
    - Alertas podem ser disparados se o usuário se aproxima ou excede o orçamento de uma categoria.

  - [ ] **Limites de Transações/Categorias**: Pode haver um limite para o número de transações ou categorias que um usuário pode ter (especialmente se você pensar em diferentes planos de usuário no futuro).

  - [ ] **Imutabilidade de Transações Antigas (Opcional)**: Você pode definir uma regra que impeça a modificação ou exclusão de transações muito antigas (ex: mais de 6 meses), para manter a integridade histórica dos dados financeiros.
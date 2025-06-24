# REQUISITOS NÃO FUNCIONAIS

Estes são atributos de qualidade do sistema:

- [ ] **Desempenho**: A API deve ser rápida e responsiva, mesmo com um volume crescente de dados. O FastAPI já é otimizado para isso.

- **Segurança**:
  - [ ]  **Proteção contra ataques comuns**: Injeção de SQL, XSS, CSRF (o FastAPI ajuda a mitigar muitos deles).
  - [ ]  **Senhas Hashing**: Armazenar senhas de usuários usando algoritmos de hash seguros (ex: bcrypt, Argon2).
  - [ ]  **Tokens JWT Seguros**: Utilizar tokens de acesso para autenticação, com expiração e renovação.
  - [ ]  **HTTPS**: A comunicação entre o cliente e a API deve ser via HTTPS para criptografia dos dados.
  
- [ ] **Usabilidade (da API)**: Os endpoints devem ser intuitivos e fáceis de usar para quem for consumir a API (seja um frontend ou outro serviço).
- [ ] **Manutenibilidade**: O código deve ser bem estruturado, modular e fácil de entender e modificar por outros desenvolvedores.
- [ ] **Confiabilidade**: O sistema deve ser robusto e capaz de lidar com falhas de forma elegante, sem perder dados ou travar.
- [ ] **Escalabilidade**: A arquitetura deve permitir que o sistema cresça e lide com mais usuários e dados no futuro.
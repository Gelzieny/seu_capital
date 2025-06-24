<p align="center">
  <a href="#">
    🔗 Seu Capital
  </a>
</p>

<p align="center">
 <a href="#-sobre-o-projeto">Sobre</a> •
 <a href="#-descricao">Descrição</a> •
 <a href="#-documentacao">Documentação</a> •
 <a href="#-layout">Layout</a> • 
 <a href="#-funcionalidades">Funcionalidades</a> • 
 <a href="#-tecnologias">Tecnologias</a> • 
 <a href="#-como-executar-o-projeto">Como executar</a> • 
 <a href="#-autor">Autor</a> • 
 <a href="#user-content--licença">Licença</a>
</p>


## Documentação

A documentação do projeto está disponível nos:

  - [Funcionalidades Essenciais (o que o sistema fará)](.github/docs/funcionalidades.md)
  - [Requisitos Funcionais (o que o sistema DEVE fazer)](.github/docs/requisitos_funcionais.md)
  - [Requisitos Não-Funcionais (como o sistema DEVE ser)](.github/docs/requisitos_nao_funcionais.md)
  - [Regras de Negócio (lógica específica do domínio financeiro)](.github/docs/regra_de_negocio.md)

  **Modelagem de Dados**

  - [Modelo de Dados](.github/docs/modelo_de_dados.md)

## 🛠 Tecnologias

<p align="justify">Este projeto utiliza um conjunto de tecnologias modernas para garantir uma aplicação eficiente e escalável, incluindo:</p>

- 🐍 **[Python](URL_ADDRESSw.python.org/)**: Linguagem de programação principal para o desenvolvimento do backend.
- 🐘 **[FastAPI](URL_ADDRESStapi.tiangolo.com/)**: Framework web moderno para construir APIs RESTful.
- 🐳 **[Docker Compose](https://docs.docker.com/compose/)**: Ferramenta para configurar e executar múltiplos containers Docker.
- 🐘 **[Postgres](https://www.postgresql.org/)**: Banco de dados relacional utilizado para armazenamento de dados.

## 🚀 Como executar o projeto

### Pré-requisitos

<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,nodejs,docker,vscode" />
</a>


### Clone o repositório

```bash
# Clone este repositório
$ git clone <https://github.com/Gelzieny/seu_capital.git>

# Acesse a pasta do projeto no terminal/cmd
$ cd seu_capital
```
### Criar e Ativar Venv e Instalar Pacotes

```bash
# Para Sistemas Linux e macOS
$ python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Para Sistemas Windows
$ python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt
```
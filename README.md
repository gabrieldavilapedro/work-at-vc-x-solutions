# Projeto de API REST para Biblioteca
## Descrição

Este é um projeto de uma API REST para gerenciar uma biblioteca de livros.

## Funcionalidades

- **Importar novos autores** por meio de um arquivo `.csv`.
- **Listar todos os autores**.
- **Filtrar autores** pelo nome.
- **Listar todos os livros**.
- **Filtrar livros** por:
    - Nome
    - Edição
    - Ano de publicação
    - Autor
- **Criar um livro**.
- **Atualizar um livro**.
- **Excluir um livro**.

## Rodando Localmente

1. **Clone o repositório**: Execute o seguinte comando no terminal:

```bash
git clone git@github.com:gabrieldavilapedro/work-at-vc-x-solutions
```

2. **Entre na pasta do projeto:**

```bash
cd work-at-vc-x-solutions
```

3. **Após clonar o repositório, crie as variáveis de ambiente:**

```bash
cp .env.example .env
```

Esse comando cria um arquivo ignorado pelo git, nele você pode alterar as variáveis de ambiente para o desenvolvimento local.

4. **Crie e ative o ambiente virtual:**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

5. **Agora instale as dependências:**

```bash
pip install -r requirements.txt
```

### Configurando o Banco de Dados PostgreSQL

Atente-se para usar o mesmo usuário, senha e nome do banco de dados nos comandos a seguir que são configurados no `.env`.

1. **Atualizar o Sistema**

Antes de instalar o PostgreSQL, certifique-se de que seu sistema está atualizado. Abra o terminal e execute os seguintes comandos:

```bash
sudo apt update && sudo apt upgrade -y
```

2. **Instalando o PostgreSQL**

```bash
sudo apt install postgresql postgresql-contrib -y
```

3. **Iniciando e Habilitando o PostgreSQL**

```bash
sudo systemctl start postgresql

sudo systemctl enable postgresql
```

4. **Acessando o PostgreSQL**

Por padrão, o PostgreSQL cria um usuário chamado `postgres`. Para acessar o PostgreSQL, você precisa mudar para este usuário:

```bash
sudo -i -u postgres
```

Em seguida, abra o prompt do PostgreSQL:

```bash
psql
```

Você verá o prompt do PostgreSQL (`postgres=#`), onde poderá executar comandos SQL.

5. **Criando um Banco de Dados**

```sql
CREATE DATABASE library;
```

6. **Crie um novo usuário:**

```sql
CREATE USER nome_do_usuario WITH PASSWORD 'senha_do_usuario';
```

7. **Conceda permissões ao usuário para acessar o banco de dados:**

```sql
GRANT ALL PRIVILEGES ON DATABASE library TO nome_do_usuario;
```

### Rodando o Servidor

1. **Rode as migrações**: Após configurar o banco de dados, execute o comando abaixo para aplicar as migrações:

```bash
python manage.py migrate
```

2. **Popular a tabela de autores**: É possível popular a tabela de autores importando um arquivo CSV com nomes, rode este comando:

```bash
python manage.py import_authors authors_exemple.csv 
```

> **Nota:** "authors_exemple.csv" é o caminho do arquivo CSV. Você pode importar qualquer arquivo que possua a coluna `name` e nomes de autores.

3. **Iniciar o servidor**: Execute o comando abaixo para iniciar o servidor:

```bash
python manage.py runserver
```

## Rodando os Testes

Também é possível rodar os testes com o seguinte comando:

```bash
python3 -m pytest
```
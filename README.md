# Projeto de API REST para Biblioteca

## Descrição

Este é um projeto de uma API REST para gerenciar uma biblioteca de livros.

Este projeto foi desenvolvido no ubuntu 22.04 em um notebook Acer Nitro AN515-51, usando o editor de texto Visual studio code. Utilizando o Python na versão **3.11.10** e o PostgreSQL na versão **14.13**.

## Funcionalidades

- **Importar novos autores** por meio de um arquivo `.csv`.
- **Listar todos os autores (Com paginação)**.
    - **Filtrar autores** pelo nome.
- **Criar um livro**.
- **Atualizar um livro**.
- **Excluir um livro**.
- **Listar todos os livros (Com paginação)**.
    - **Filtrar livros** por:
        - Nome;
        - Edição;
        - Ano de publicação;
        - Autor.

## Configurando o Banco de Dados PostgreSQL

**Segue as instruções de instalação do postgres no sistema operacional ubuntu, isso pode ser diferente dependendo do sistema operacional.**

1. Atualizar o Sistema

Antes de instalar o PostgreSQL, certifique-se de que seu sistema está atualizado. Abra o terminal e execute os seguintes comandos:

```bash
sudo apt update && sudo apt upgrade -y
```

2. Instalando o PostgreSQL

```bash
sudo apt install postgresql postgresql-contrib -y
```

3. Iniciando e Habilitando o PostgreSQL

```bash
sudo systemctl start postgresql
```

```bash
sudo systemctl enable postgresql
```

**Após a instalação siga os seguintes passos:**

1. **Acessando o PostgreSQL**

Por padrão, o PostgreSQL cria um usuário chamado `postgres`. Para acessar o PostgreSQL, você precisa mudar para este usuário:

```bash
sudo -i -u postgres
```

Em seguida, abra o prompt do PostgreSQL:

```bash
psql
```

Você verá o prompt do PostgreSQL (`postgres=#`), onde poderá executar comandos SQL.

2. Criando um Banco de Dados

**Atente-se para usar o mesmo usuário, senha e nome do banco de dados nos comandos a seguir que são configurados no `.env`.**

```sql
CREATE DATABASE library;
```

6. Crie um novo usuário:

```sql
CREATE USER nome_do_usuario WITH PASSWORD 'senha_do_usuario';
```

7. Conceda permissões ao usuário para acessar o banco de dados:

```sql
GRANT ALL PRIVILEGES ON DATABASE library TO nome_do_usuario;
```

8. Conceda a permissão de criação de banco de dados ao usuário (substitua nome_do_usuario pelo nome do usuário do banco de dados):

```sql
ALTER USER nome_do_usuario CREATEDB;
```

9. Para sair do prompt do PostgreSQL (postgres=#), você pode usar o comando `\q` e em seguida `exit`

## Rodando Localmente

1. Clone o repositório: Execute o seguinte comando no terminal:

```bash
git clone git@github.com:gabrieldavilapedro/work-at-vc-x-solutions
```

2. Entre na pasta do projeto:

```bash
cd work-at-vc-x-solutions
```

3. Após clonar o repositório, crie as variáveis de ambiente:

```bash
cp env.example .env
```

Esse comando cria um arquivo ignorado pelo git, nele você pode alterar as variáveis de ambiente para o desenvolvimento local.

4. Crie e ative o ambiente virtual:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

5. Agora instale as dependências:

```bash
pip install -r requirements.txt
```

6. **Rode as migrações**: Após configurar o banco de dados, abra um novo terminal com o .venv ativo e execute o comando abaixo para aplicar as migrações:

```bash
python manage.py migrate
```

7. **Popular a tabela de autores**: É possível popular a tabela de autores importando um arquivo CSV com nomes, rode este comando:

```bash
python manage.py import_authors authors_exemple.csv 
```

"authors_exemple.csv" é o caminho do arquivo CSV. Você pode importar qualquer arquivo que possua a coluna `name` e nomes de autores. Esse script ira inserir os autores no banco em lotes, você pode opcionalmente controlar o tamanho desses lotes passando o argumento `--batch_size=1000`

8. **Iniciar o servidor**: Execute o comando abaixo para iniciar o servidor:

```bash
python manage.py runserver
```
Após realizar estes passos, já será possível fazer as requisições para a API.

## Documentação das Rotas


Faça o download deste arquivo, onde estão documentadas as rotas:

[Library.postman](./Library.postman_collection.json)

### Importando no Postman

1. Abra o Postman.
2. Clique no botão `Import` no canto superior esquerdo.
3. Selecione a aba `File`.
4. Selecione o arquivo `Project-blogs-api.postman` que você baixou.
5. Clique em `Import`.

Após importar, você verá todas as rotas documentadas no Postman e poderá fazer as requisições diretamente.

### Exemplo de Uso

Aqui está um exemplo de como fazer uma requisição usando o Postman:

1. Selecione a rota que você deseja testar;
2. Configure os parâmetros necessários. a documentação possui exemplos;
3. Clique em `Send` para enviar a requisição;
4. Veja a resposta no painel de resposta do Postman.

Com essas instruções, você deve ser capaz de baixar e importar o arquivo de configuração do Postman e começar a fazer requisições para a API documentada.

## Rodando os Testes

Também é possível rodar os testes com o seguinte comando:

```bash
python3 -m pytest
```
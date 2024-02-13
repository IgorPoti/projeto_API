<br/>
<p align="center">
  <a href="https://github.com/IgorPoti/projeto_API">
    <img src="https://cdn.worldvectorlogo.com/logos/fastapi.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">API com FastAPI</h3>

  <p align="center">
    API para fins de estudos com FastAPI. No projeto foi gerado diversos endpoints para usuários e inserção de artigos (CRUD) com autorização OAuth 2.0.
    <br/>
    <br/>
    <a href="https://github.com/IgorPoti/projeto_API"><strong>Um pouco sobre o projeto »</strong></a>
    <br/>
    <br/>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/IgorPoti/projeto_API?color=dark-green) ![Forks](https://img.shields.io/github/forks/IgorPoti/projeto_API?style=social) ![Stargazers](https://img.shields.io/github/stars/IgorPoti/projeto_API?style=social) ![Issues](https://img.shields.io/github/issues/IgorPoti/projeto_API) 

## Sobre o projeto

![Screen Shot](https://cdn.discordapp.com/attachments/1069309703072518146/1207031523552002128/image.png?ex=65de2ab4&is=65cbb5b4&hm=d765d9feeca8e1a8b6f6743900688f6ce8305798dd54378a50d2e79728e6e2a3&)

**Documentação do Módulo de Artigos**

| Endpoint                      | Descrição                                                        | Parâmetros de Entrada                                | Resposta de Sucesso (Código 200)                        | Possíveis Erros                               |
|-------------------------------|------------------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|-----------------------------------------------|
| **POST /artigos**             | Cria um novo artigo.                                             | `artigo` (ArtigoSchema), `usuario_logado` (UsuarioModel), `db` (AsyncSession) | Retorna os detalhes do artigo recém-criado no formato JSON conforme definido pelo esquema `ArtigoSchema`. | Código 404: Usuário não logado                                             |
| **GET /artigos**              | Retorna a lista de todos os artigos.                             | `db` (AsyncSession)                                   | Retorna uma lista de detalhes dos artigos no formato JSON conforme definido pelo esquema `ArtigoSchema`. | Código 404: Artigo não encontrado                                             |
| **GET /artigos/{artigo_id}**  | Retorna os detalhes de um artigo específico.                     | `artigo_id` (int), `db` (AsyncSession)                | Retorna os detalhes do artigo no formato JSON conforme definido pelo esquema `ArtigoSchema`. | Código 404: Artigo não encontrado.            |
| **PUT /artigos/{artigo_id}**  | Atualiza os detalhes de um artigo específico.                    | `artigo_id` (int), `artigo` (ArtigoSchema), `db` (AsyncSession), `usuario_logado` (UsuarioModel) | Retorna os detalhes atualizados do artigo no formato JSON conforme definido pelo esquema `ArtigoSchema`. | Código 404: Artigo não encontrado.            |
| **DELETE /artigos/{artigo_id}**| Exclui um artigo específico.                                     | `artigo_id` (int), `db` (AsyncSession), `usuario_logado` (UsuarioModel) | Retorna uma resposta vazia indicando que o artigo foi excluído com sucesso. | Código 404: Artigo não encontrado.          |


### Esquemas Utilizados

- **`ArtigoSchema`**: Esquema para representar os detalhes de um artigo.

### Dependências Utilizadas

- **`get_session`**: Função para obter uma sessão do banco de dados.
- **`get_current_user`**: Função para obter o usuário atualmente autenticado.


**Documentação do Módulo de Usuários**

| Endpoint                    | Descrição                                           | Parâmetros de Entrada                                         | Resposta de Sucesso (Código 200)                                | Possíveis Erros                           |
|-----------------------------|-----------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------|
| **GET /logado**             | Retorna os detalhes do usuário logado.               | Nenhum (usa o token de autenticação).                         | Retorna os detalhes do usuário logado no formato JSON conforme definido pelo esquema `UsuarioSchemaBase`. | -                                         |
| **POST /signup**            | Cria um novo usuário.                                | `nome` (str), `sobrenome` (str), `email` (str), `senha` (str), `eh_admin` (bool, opcional) | Retorna os detalhes do usuário recém-criado no formato JSON conforme definido pelo esquema `UsuarioSchemaBase`. | Código 406: Já existe um usuário com o mesmo e-mail cadastrado. |
| **GET /usuarios**           | Retorna a lista de todos os usuários.                | Nenhum (usa o token de autenticação).                         | Retorna uma lista de detalhes do usuário no formato JSON conforme definido pelo esquema `UsuarioSchemaBase`. | -                                         |
| **GET /{usuario_id}**       | Retorna os detalhes de um usuário específico.        | `usuario_id` (int)                                           | Retorna os detalhes do usuário no formato JSON conforme definido pelo esquema `UsuarioSchemaArtigos`. | Código 404: Usuário não encontrado.        |
| **PUT /{usuario_id}**       | Atualiza os detalhes de um usuário específico.       | `usuario_id` (int), `nome` (str, opcional), `sobrenome` (str, opcional), `email` (str, opcional), `eh_admin` (bool, opcional), `senha` (str, opcional) | Retorna os detalhes atualizados do usuário no formato JSON conforme definido pelo esquema `UsuarioSchemaBase`. | Código 404: Usuário não encontrado.       |
| **DELETE /{usuario_id}**    | Exclui um usuário específico.                        | `usuario_id` (int)                                           | Retorna uma resposta vazia indicando que o usuário foi excluído com sucesso. | Código 404: Usuário não encontrado.       |
| **POST /login**             | Realiza a autenticação do usuário e retorna um token de acesso. | `username` (str), `password` (str)                           | Retorna um token de acesso no formato JSON.                    | Código 400: Dados de acesso incorretos.  |

### Esquemas Utilizados

- **`UsuarioSchemaBase`**: Esquema base para representar os detalhes do usuário.
- **`UsuarioSchemaCreate`**: Esquema para validar os dados durante o cadastro de um novo usuário.
- **`UsuarioSchemaUp`**: Esquema para validar os dados durante a atualização de um usuário.
- **`UsuarioSchemaArtigos`**: Esquema para representar os detalhes do usuário, incluindo informações sobre artigos relacionados.

### Dependências Utilizadas

- **`get_session`**: Função para obter uma sessão do banco de dados.
- **`get_current_user`**: Função para obter o usuário atualmente autenticado.
- **`gerar_hash_senha`**: Função para gerar o hash da senha do usuário.
- **`autenticar`**: Função para autenticar o usuário durante o login.
- **`criar_token_acess`**: Função para criar um token de acesso após a autenticação.




## Construído com

- **FastAPI**: Framework web assíncrono para construção de APIs rápidas em Python.
- **SQLAlchemy**: Biblioteca para interação com bancos de dados SQL em Python.
- **Pydantic**: Biblioteca para validação de dados usando modelos Python.
- **OAuth2**: Padrão de autenticação utilizado para segurança em endpoints.
- **JWT (JSON Web Tokens)**: Método para gerar tokens de acesso seguros.
- **Jose**: Biblioteca para trabalhar com JWT (JSON Web Tokens) em Python.

# API-Delfos

Para poder executar a aplicação, será necessário a intalação do Docker e do Pipenv

Obs.: A implementação foi realizada no Windows, logo para executar em linux, pode haver a necessidade de ajustar os **imports**

----------------------------------------------------------------------------------------------------------------------------------

1) Entrar no diretório onde o repositório foi instalado e executar o comando:

   **docker-compose up -d**
   
----------------------------------------------------------------------------------------------------------------------------------

2) Após subir as imagens do Docker, será necessário iniciar o ambiente virtual do Pipenv. Para isso executamos os seguintes comandos:

   **pipenv shell**
   **pipenv update**

   Obs.: O pipenv já baixa todas as dependências citadas dentro do arquivo: **Pipfile**
  
---------------------------------------------------------------------------------------------------------------------------------

3) Será necessário entrar no endereço: localhost:5050 e iniciar dois servidores.
    - O primerio servidor com o Banco de Dados Fonte:

     ![image](https://github.com/DiegoBasgal/API-Delfos/assets/73798718/16f4984d-896f-488e-abdb-4b590789aed2)

    - O mesmo deverá ser feito para o Banco de Dados Alvo:

    ![image](https://github.com/DiegoBasgal/API-Delfos/assets/73798718/4d4af22e-3a7c-4f8d-b2e1-141ecd3b551a)


  Obs.: Usuário -> admin | Senha -> admin

---------------------------------------------------------------------------------------------------------------------------------

4) Após a criação dos Bancos de Dados, será necessário popular o Banco de Dados Fonte. Para isso será necessário executar o script
   dentro do arquivo **populate_font_database.py**

---------------------------------------------------------------------------------------------------------------------------------

5) Após popular o Banco de Dados fonte, será necessário iniciar os serviços do **FastAPI** e **Dagster**, para isso executamos os
   seguintes comandos em dois terminais separados:
  
   - FastAPI -> **uvicorn main:app --port 8080 --reload**
   - Dagster -> **dagster dev**
  
   Obs.: Para acessar as páginas dos módulos, digitar na url do navegador:
     - FastAPI -> 127.0.0.1:8080
     - Dagster -> 127.0.0.1:3000

--------------------------------------------------------------------------------------------------------------------------------

6) Para executar o pipeline, **acessar a url do dagster -> deployment -> acessar o repositório -> jobs -> etl_pipeline -> launchpad**
   e executar o **Launch Run**

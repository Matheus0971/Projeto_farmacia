# Farmácia - Trabalho [ DCDII ]  
Tema: Farmácia  
Grupo: Matheus Henrique, Luís Felipe e Rebeca Araujo  
Usuários do git:  
● Matheus: https://github.com/Matheus0971  
● Luis: https://github.com/felipe-kutscher  
● Rebeca: https://github.com/Rebeca-AB  
Pergunta: Qual funcionário vendeu mais?  
Proposta: Farmácia. Tabelas `farmaceuticos`, `produtos` e `vendas`, ligadas por `farmaceutico_id` e `produto_id`.

## E1 - O banco e o Model do seu negócio:  


## Como rodar o projeto
1. Instale as dependências:
```
pip install -r requirements.txt
```
2. Copie o arquivo `.env.exemplo` para `.env` e preencha as variáveis de conexão do PostgreSQL (`PGHOST`, `PGPORT`, `PGDATABASE`, `PGUSER`, `PGPASSWORD`) e do MongoDB (`MONGO_URI`).
3. Crie as tabelas e popule o banco relacional:
```
python criar_tabelas.py
python popular.py
```
4. Suba a API FastAPI e acesse `/docs`:
```
uvicorn main:app --reload
```
5. Execute os testes automatizados:
```
python -m pytest -q
```
6. Execute a análise de vendas (gera o gráfico `grafico_vendas.png`):
```
python analise.py
```

## Resposta da análise
Fernanda Lima é a vendedora que mais vendeu: **R$ 1311.00** (**38.7%** do faturamento total de R$ 3384.50), seguida por Mariana Souza (R$ 752.00) e Carlos Eduardo (R$ 559.00). Embora a expectativa inicial fosse que medicamentos básicos liderassem o faturamento, o volume de dermocosméticos (como protetor solar) fez com que Fernanda Lima ficasse bem à frente dos demais vendedores.

## E3 - Item à escolha: MongoDB
**Por que MongoDB e não processamento paralelo?** Escolhemos o MongoDB, pois os produtos da farmácia tem detalhes diferentes, como por exemplo, remédios tem princípio ativo e dosagem e o protetor solar tem FPS. No MongoDB cada produto é um documento com os campos que precisa, sem colunas vazias. Não escolhemos o paralelismo porque a nossa base é pequena e não daria para medir um ganho de tempo.

**Como ficou:** O banco farmacia do Atlas tem a coleção fichas, com uma ficha por produto. O campo rotulo é o nome do produto no PostgreSQL e liga a ficha ao produto.

| Arquivo | O que faz |
|---|---|
| `mongo_conexao.py` | Lê o MONGO_URI do .env, conecta no Atlas e escolhe o banco/colecao |
| `mongo_popular.py` | Apaga o que existe e insere as 10 fichas com insert_many |
| `mongo_consultar.py` | Funciona como um Find, filtra o que existe no banco |
| `mongo_alterar.py` | Faz atualizações no banco |

**Como rodar o MongoDB**
1. No Atlas (cloud.mongodb.com), crie um cluster gratuito (M0), crie um usuário com senha e libere o seu IP em *Database & Network Access*.
2. Em *Connect > Drivers > Python*, copie a string de conexão e cole no .env como MONGO_URI, trocando o "<db_password>" pela senha (sem os sinais < e >).
3. Rode os scripts nesta ordem:

```
python mongo_popular.py     # insere os dados
python mongo_alterar.py   # altera e apaga
python mongo_consultar.py     # faz consultas no banco
```

O mongo_alterar.py apaga uma ficha. Para reinicar, rode o mongo_popular.py novamente.

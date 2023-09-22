# Pipeline ETL Utilizando IA Generativa com Python e Pandas

Projeto baseado no desafio Santander Bootcamp 2023 Ciência de Dados, que consistia na construção de uma Pipeline ETL
Houve a EXTRAÇÃO dos dados de um tabela CSV utilizando a biblioteca Pandas e a criação de variáveis contendo listas 
que representavam colunas da tabela, sendo elas: 'UserID', contendo um código para cada nome, 'Name' contento os nomes,
'Age', contendo as idades e por fim 'City', contendo as cidades.
Utilizando a API do openAI foi criado uma função que cria uma lista vazia e também geradora de mensagens personalizadas 
para as pessoas listadas na tabela CSV. A IA Generativa foi orientada a se tornar um especialista em Turismo e direcionar 
as pessoas, mensagens citando suas respectivas cidades e considerando ainda a faixa etária.  
Em seguida a função foi utilizada para armazenamento das mensagens na tabela CSV numa nova coluna chamada 'Messages', 
concluindo a fase TRANSFORMAÇÃO.
Por fim o arquivo foi novamente manipulado com o módulo Pandas para ser salvo com os dados enriquecidos, concluindo a fase
de CARREGAMENTO (LOAD).


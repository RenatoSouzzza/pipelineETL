# Projeto baseado no desafio Santander Bootcamp 2023 Ciência de Dados, que consistia na construção de uma Pipeline ETL.
# Houve a EXTRAÇÃO dos dados de um tabela CSV utilizando a biblioteca Pandas e a criação de variáveis contendo listas 
# que representavam colunas da tabela, sendo elas: 'UserID', contendo um código para cada nome, 'Name' contento os nomes,
# 'Age', contendo as idades e por fim 'City', contendo as cidades.
# Utilizando a API do openAI foi criado uma função que cria uma lista vazia e também geradora de mensagens personalizadas 
# para as pessoas listadas na tabela CSV. A IA Generativa foi orientada a se tornar um especialista em Turismo e direcionar 
# as pessoas, mensagens citando suas respectivas cidades e considerando ainda a faixa etária.  
# Em seguida a função foi utilizada para armazenamento das mensagens na tabela CSV numa nova coluna chamada 'Messages', 
# concluindo a fase TRANSFORMAÇÃO.
# Por fim o arquivo foi novamente manipulado com o módulo Pandas para ser salvo com os dados enriquecidos, concluindo a fase
# de CARREGAMENTO (LOAD).

import pandas as pd
data = pd.read_csv( 'dados_projeto.csv' ) # Extaction

user = data['UserID'].tolist()
name = data['Name'].tolist()
age = data['Age'].tolist()
city = data['City'].tolist()

chave_openAI = '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'

import openai

openai.api_key = chave_openAI

def gerador_msg(name, age, city):
    mensagens = []
    for i in range(len(user)):
        completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em turismo"
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {name[i]} sobre atrações turísticas na cidade {city[i]} considerando a faixa etária {age[i]} de cada um deles (máximo de 100 caractéres)"
            }
        ]
        )
        response = completion.choices[0].message.content.strip('\"')
        mensagens.append(response)
    return mensagens

mensagens = gerador_msg(data['Name'].tolist(), data['Age'].tolist(), data['City'].tolist()) # Transformation
data['Messages'] = mensagens
data.to_csv('dados_projeto.csv', index=False) # Load
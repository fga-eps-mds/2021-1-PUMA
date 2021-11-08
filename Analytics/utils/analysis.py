ANALYSIS = {
    'ProjectService':\
'''
## Project Service

Percebe-se que no serviço de projetos o desempenho de testes foi apenas realizado após algumas sprints.
Isso ocorreu pois foi priorizada a entrega de histórias de usuários que ficaram atrasadas por falhas durante
a gestão do time, que desempenhou menos que o esperado, necessitando, então, a entrada do time de EPS no desenvolvimento.
''',
    'ApiGateway':\
'''
## Api Gateway

No Gateway, por ser um serviço de intermediação de requisição foram feitos apenas testes de integração, e não foi possível gerar a coleta desses dados para
a análise.
''',
    'UserService':
'''
## User Service

* Complexidade
    - A complexidade manteve uma constância durante todas as releases geradas e ao final, com uma refatoração, pode-se perceber uma melhora.
* Sucesso nos testes
    - Nas primeiras releases não foram desenvolvidos testes devido a diversos fatores, desde trancamento de integrantes do grupo até um desempenho abaixo do esperado nas entregas de histórias de usuário. Dessa forma, o gráfico se manteve constante, até a última release, onde foi possível realizar essas ''',
    'Frontend':\
'''
## Frontend

No forntend não foi possível a geração de testes.
'''
}

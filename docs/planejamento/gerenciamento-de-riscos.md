# Plano de Gerenciamento de Riscos
| Data | Versão | Autores | Descrição |
|--|--|--|--|
| 11/09/2021 | 1.0 | Luís Taira | Criação do documento |

## Participantes
| Participante | 
|--------------|
| Luís Taira |

## Escopo
Este documento visa 

## Riscos e suas consequências

### Riscos de projeto:

### Riscos técnicos
| ID | Risco | Consequêcia |
|--|--|--|
| 1 | Dificuldade com as tecnologias escolhidas | Atraso e diminuição da qualidade das entregas  |

### Riscos de gerenciamento
| ID | Risco | Consequêcia |
|--|--|--|
| 2 | Mudança na arquitetura | Gera retrabalho, mais trabalho, impede temporariamente a produção do grupo |
| 3 | Mudança de escopo | Alteração no cronograma e redefinição de requisitos |
| 4 | Falha na comunicação | Erros no projeto e discórdia no time |
| 5 | Imaturidade na gerência | Diminui a qualidade e gera atraso nas entregas |


### Riscos organizacionais
| ID | Risco | Consequêcia |
|--|--|--|
| 6 | Desistência de membros | Sobrecarga dos membros remanescentes |
| 7 | Atraso nas entregas | Diminui a qualidade do produto |
| 8 | Discórdia entre os membros do grupo | Diminui o comprometimento dos membros e a qualidade das entregas |

### Riscos externos
| ID | Risco | Consequêcia |
|--|--|--|
| 9 | Problemas de saúde entre os membros  | Atraso nas entregas e falta nas reuniões |
| 10 | Greve na UnB | O projeto fica inviável

<hr>

### Riscos de produto
| ID | Risco | Consequêcia |
|--|--|--|
| 11 | Não ter onde hospedar o produto | O produto fica inutilizável depois que o semestre acabar |


## Probabilidade x Impacto

Probabilidade | % de certeza | Peso
|--|--|--|
Nula | 0% | 0
Muito baixa | 0 a 20% | 1
Baixa | 20 a 40% | 2
Média | 40 a 60% | 3
Alta | 60 a 80% | 4
Muito alta | 80 a 100% | 5

Impacto | Impacto sobre o Custo Original (%) | Peso
|--|--|--|
Nulo | 0% | 0
Muito baixo | 1 a 5% | 1
Baixo | 5 a 10% | 2
Médio | 10 a 15% | 3
Alto | 15 a 20% | 4
Muito alto | Acima de 20% | 5

### O grau de risco é definido pela multiplicação da probabilidade pelo impacto. Conforme tabela abaixo:

![](https://i.imgur.com/UgqOw1k.png)

Sendo que:

1. Risco >= 15: Elevado
2. 5 < Risco < 15: Médio
3. Risco =< 5: Baixo

<table class="table table-hover">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Descrição</th>
            <th scope="col">Probabilidade</th>
            <th scope="col">Impacto</th>
            <th scope="col">Risco</th>
        </tr>
    </thead>
    <tbody>
        <tr class="table-danger">
            <th scope="row">6</th>
            <td>Desistência de membros</td>
            <td> 4 </td>
            <td> 5 </td>
            <td> 20 </td>
        </tr>
        <tr class="table-danger">
            <th scope="row">2</th>
            <td>Mudança na arquitetura</td>
            <td>5</td>
            <td>3</td>
            <td>15</td>
        </tr>
        <tr class="table-warning">
            <th scope="row">5</th>
            <td>Imaturidade na gerência</td>
            <td> 3 </td>
            <td> 4 </td>
            <td> 12 </td>
        </tr>
        <tr class="table-warning">
            <th scope="row">7</th>
            <td>Atraso nas entregas</td>
            <td> 5 </td>
            <td> 2 </td>
            <td> 10 </td>
        </tr>
        <tr class="table-warning">
            <th scope="row">9</th>
            <td>Problemas de saúde entre os membros</td>
            <td> 5 </td>
            <td> 2 </td>
            <td> 10 </td>
        </tr>
        <tr class="table-warning">
            <th scope="row">4</th>
            <td>Falha na comunicação</td>
            <td> 4 </td>
            <td> 4 </td>
            <td> 8 </td>
        </tr>
        <tr class="table-warning">
            <th scope="row">1</th>
            <td>Dificuldade com as tecnologias escolhidas</td>
            <td> 3 </td>
            <td> 3 </td>
            <td> 6 </td>
        <tr class="table-warning">
            <th scope="row">8</th>
            <td>Discórdia entre os membros do grupo</td>
            <td> 3 </td>
            <td> 5 </td>
            <td> 6 </td>
        </tr>
        </tr>
        <tr class="table-info">
            <th scope="row">3</th>
            <td>Mudança de escopo</td>
            <td>2</td>
            <td> 3 </td>
            <td> 5 </td>
        </tr>
        <tr class="table-info">
            <th scope="row">10</th>
            <td>Greve na UnB</td>
            <td> 1 </td>
            <td> 5 </td>
            <td> 5 </td>
        </tr>
        <tr class="table-info">
            <th scope="row">11</th>
            <td>Não ter onde hospedar o produto</td>
            <td> 1 </td>
            <td> 5 </td>
            <td> 5 </td>
        </tr>
    </tbody>
</table>
<br>
<br>

## Planejamento de resposta aos riscos

| # | Descrição | Risco | Ação | Descrição da ação | Responsável |
| -- | -- | -- | -- | -- | -- |
| 1 | Dificuldade com as tecnologias escolhidas | 6 | Previnir | Realizar treinamentos e acompanhar diariamente o aprendizado das tecnologias | Time de EPS |
| 2 | Mudança na arquitetura | 15 | Mitigar | Ter certeza que a arquitetura está adequada através de pesquisas e realizar a transição da forma menos prejudicial possível | João |
| 3 | Mudança de escopo | 5 | Previnir | Construindo o escopo continuamente com os stakeholders | Samuel |
| 4 | Falha na comunicação | 8 | Previnir | Incentivando os rituais ágeis e a boa comunicação do time | Luís |
| 5 | Imaturidade na gerência | 12 | Mitigar | Se esforçando par gerir o time com responsabilidade e tendo boa comunicação com MDS e o professor | Time de EPS |
| 6 | Desistência de membros | 20 | Aceitar | Realocar tarefas | Luís |
| 7 | Atraso nas entregas | 10 | Previnir | Realizando os rituais ágeis, mantendo a boa comunicação do time, promovendo o compartilhamento de conhecimento e acompanhando o andamento de cada issue | Luís | 
| 8 | Discórdia entre os membros do grupo | 6 | Previnir | Promovendo a boa comunicação e evitando a antagonização de membros | Luís |
| 9 | Problemas de saúde entre os membros | 9 | Previnir | Evitando a contaminação com COVID-19 e outras doenças infecciosas e não realizando ações que impediriam a colaboração com o time em horas ou dias futuros | Todo o time |
| 10 | Greve na UnB | 5 | Aceitar | Planejar a execução do projeto quando for possível | Luís |
| 11 | Não ter onde hospedar o produto | 5 | Previnir | Ter certeza que, quando a matéria acabar, o produto estará bem hospedado de uma forma que os stakeholders possam mantê-lo | Eduardo |
# Backlog do Produto 
| Data | Versão | Autores | Descrição |
|--|--|--|--|
| 03/09/2021 | 0.9 | Artur Vinicius, Eduardo Lima, Gabriel Tiveron, João Pedro, Luís Taira, Samuel Pereira | Criação do documento |
| 08/09/2021 | 1.0 | Eduardo Lima, Gabriel Tiveron, João Pedro, Luís Taira, Samuel Pereira | Adição de features e PBIs |
| 10/09/2021 | 1.1 | Eduardo Lima, Gabriel Tiveron, Luís Taira, Samuel Pereira, Nícolas, Giulia e Artur | Adição de features e PBIs |

## Histórias de Usuário
| Número | Eu, como | posso | para |
|--|--|--|--|
| US01 | Usuário | fazer cadastro | ter acesso ao PUMA |
| US02 | Usuário | fazer login | acessar o PUMA |
| US03 | Agente Externo | registrar proposta de projeto | resolver um problema |
| US04 | Professor | visualizar uma proposta | avaliá-la |
| US05 | Usuário | redefinir minha senha | continuar tendo acesso à minha conta |

# Feature

- Fazer cadastro de usuário
    - Problema:
        - Diferenciar usuários
    - Benefício:
        - Acessar o PUMA
    - PBI:
        - Ter acesso a página de cadastro do usuário (Prioridade 4)
        - Preencher ficha de cadastro do usuário (Prioridade 4)
        - Submeter ficha completa do cadastro do usuário (Prioridade 4)
    - Histórias de usuário
        - US01 - Eu como usuário porsso fazer cadastro para ter acesso ao PUMA.

- Registro de proposta
    - Problema:
        - Dificuldade de encontrar executores
        - Dificuldade de fazer proposta
    - Benefício:
        - Padronização na submissão de proposta
        - Documentação da proposta
    - PBI:
        - Navegar até a página de registro (Prioridade 4)
        - Preencher ficha de registro de proposta (Prioridade 4)
        - Submeter ficha completa de proposta (Prioridade 4)
    - Histórias de usuário
        - US02 - Eu como usuário posso fazer login para acessar o PUMA.

- Login
    - PBI:
        - Ter acesso a página de usuário (Prioridade 7)
        - Fornecer dados de usuário (Prioridade 7)
        - Ser direcionado ao sistema (Prioridade 7)
    - Histórias de usuário
        - US03 - Eu como agente externo posso registrar proposta de projeto para resolver um problema.

- Avaliação de proposta
    - Problema:
        - Serem aceitas propostas que não condizem com matérias 
    - Benefício:
        - Fazer avaliação na plataforma
    - PBI:
        - Identificar o agente responsável pelo projeto (Prioridade 7)
        - Visualizar a descrição do projeto (Prioridade 7)
    - Histórias de usuário
        - US04 - Eu como professor posso visualizar uma proposta para avaliá-la.

- Recuperação de senha
    - Problema:
        - Não conseguir acesso após esquecer a senha
    - Benefício:
        - Ter a possibilidade de recuperar a senha
    - PBI:
        - Enviar um e-mail de confirmação de recuperação de senha (Prioridade 8)
    - Histórias de usuário
        - US05 - Eu como usuário posso redefinir minha senha para continuar tendo acesso à minha conta.

- CRUD de disciplinas
    - Problema:
        - Falta de organização das disciplinas
    - Benefício:
        - Centralização das disciplinas
        - Gerência de disciplinas 
    - PBI:
        - Ter página de criar disciplina no PUMA (Prioridade 4)
        - Ter página de visualizar disciplinas com opção de remover e editar disciplina no PUMA (Prioridade 5)
        - Ter página de detalhamento de disciplina no PUMA (Prioridade 4)
        - Ter um professor cadastrado no PUMA (Prioridade 7)

- Página de detalhamento de projeto
    - Problema:
        - Não saber do que se trata a proposta
        - Não conseguir identificar facilmente o agente responsável
    - Benefício:
        - Fácil identificação dos detalhes do projeto
    - PBI:
        - Identificar o agente responsável pelo projeto (Prioridade 4)
        - Visualizar a descrição do projeto (Prioridade 3)

- Alocação de proposta
    - Problema:
        - Identificação a qual disciplina propostas se encaixam
        - Processo manual
    - Benefício:
        - Automatização do processo
    - PBI:
        - Visualizar o resultado da alocação de proposta (Prioridade 7)

- Página de acompanhamento da proposta
    - Problema:
        - Não ter feedback sobre o processamento da proposta
    - Benefício:
        - Poder acompanhar se a proposta foi aprovada
    - PBI:
        - Acessar a página de acompanhamento da proposta (Prioridade 3)

- CRUD de times
    - Problema:
        - Não conseguir criar ou alterar times
    - Benefício:
        - Criar ou alterar times para o desenvolvimento de um projeto
    - PBI:
        - Ter acesso à página de criar times (Prioridade 4)
        - Preencher as informações do time (Prioridade 4)
        - Adicionar participantes do time (Prioridade 4)
        - Submeter a solicitação no sistema (Prioridade 4)

- Alocação de times
    - Benefício:
        - Separar as pessoas em cada projeto
    - PBI:
        - Ter acesso a página de alocação de times (Prioridade 4)
        - Selecionar um time para cada projeto (Prioridade 4)

- Perfil de Usuário
    - Problema:
        - Não ter fácil acesso a informações pessoais
    - Benefício:
        - Conferir informações
        - Possibilitar edição
    - PBI:
        - Acessar a página de perfil (Prioridade 4)

- Página de projetos divulgados
    - Problema:
        - Não conseguir identificar projetos em destaque
    - Benefício:
        - Divulgação de projetos principais concluídos
    - PBI:
        - Acessar a página de projetos com destaque (Prioridade 4)

- Avaliação por pares
    - Problema:
        - Nescessidade de usar outra plataforma para avaliação por pares
        - Ter que criar os times em outro lugar para fazer avaliação
    - Benefício:
        - Alunos se avaliarem sem sair da plataforma
    - PBI:
        - Ter acessoa à página de avaliação por pares (Prioridade 3)
        - Reportar resultados ao professor (Prioridade 3)

- Validação de matrícula 
    - Problema:
        - Certificar-se que apenas alunos da Universidade serão cadastrados como executores
    - Benefício:
        - Apenas alunos da Universidade serão cadastrados como executores
    - PBI:
        - Validar a matrícula junto a Universidade (Prioridade 2)

- Repositório de projetos (com metadados)
    - Problema:
        - Não conseguir identificar projetos já executados
    - Benefício:
        - Divulgação de projetos concluídos
    - PBI:
        - Acessar a página de projetos concluídos (Prioridade 3)

- Página de acompanhamento de times
    - Problema:
        - Não ter informações sobre o progresso de times
    - Benefício:
        - Acompanhamento dos times
    - PBI:
        - Acessar a página de acompanhamento de times (Prioridade 2)

- Página de acompanhamento de projetos em execução
    - Problema:
        - Falta de transparência da execução do projeto
    - Benefício:
        - Atualizações sobre a execução
    - PBI:
        - Ter alunos, professores e agentes externos registrados (Prioridade 7)
        - Ter página de acompanhamento de projetos em execução (Prioridade 3)

- Manutenção do algorítmo de alocação
    - Problema:
        - Ter que acessar o código/deploy para atualizar o algorítmo
    - Benefício:
        - Atualizar os parâmetros do algorítmo na própria plataforma
    - PBI:
        - Entrar na página de manutenção do algoritmo (Prioridade 4)

- Avaliação por professores aos projetos
    - Problema:
        - Avaliar projetos concluídos como professor
    - Benefício:
        - O professor avalia o projeto na disciplina
    - PBI:
        - Entrar na página do projeto como professor (Prioridade 4)
        - Adicionar a avaliação no projeto (Prioridade 4)

- Feedback ao cliente sobre sobre a proposta
    - Problema:
        - Não ter informações sobre a proposta submetida
    - Benefício:
        - Melhorar a experiência de usuário
    - PBI:
        - Dar um feedback para o cliente sobre a aprovação da proposta divulgados (Prioridade 3)

- Página de feedback final (Relatos de stakeholders)
    - Problema:
        - Não saber a visão do agente externo sobre o projeto
    - Benefício:
        - Alunos e professores saberem qual a opinião do agente externo acerca do projeto executado.
    - PBI:
        - Acessar a página de feedback final (Prioridade 3)

- Confirmação de e-mail
    - Problema:
        - Impossibilidade de utilizar certas funcionalidades com e-mail inválido
    - Benefício:
        - Feedback de inserção de e-mail válido
    - PBI:
        - Receber o e-mail de confirmação (Prioridade 3)
        - Confirmar o e-mail do usuário (Prioridade 3)

- Acompanhamento de alterações
    - Problema:
        - Não conseguir acompanhar as atualizações do projeto
    - Benefício:
        - Melhor comunicação do time
    - PBI:
        - Visualizar as alterações na página do projeto (Prioridade 6)


# Descrição
## Usuário
### US01
#### Tarefas
 1. Fazer página de cadastro
 2. Criar a rota de cadastro no backend
 3. Conexão do frontend com o backend
 4. Armazenar informações de usuário na base de dados
 5. Retornar resultado do cadastro

#### Critérios de aceitação
 1. O usuário deve conseguir seguir o fluxo de cadastro
 2. O usuário deve estar cadastrado na base de dados
 3. Funcionalidade deve estar testada

### US02
#### Tarefas
 1. Fazer página de login
 2. Criar a rota de login no backend
 3. Conexão do frontend com o backend
 4. Autenticar informações do usuário
 5. Retornar resultado do login
 6. Redirecionar à página inicial

#### Critérios de aceitação
 1. O usuário deve conseguir seguir o fluxo de login
 2. O usuário deve ser autenticado no backend
 3. O usuário deve possuir uma sessão de acesso
 4. Funcionalidade deve estar testada

## Agente Externo
### US03
#### Tarefas
 1. Fazer página de registro de proposta de projeto
 2. Fazer o fluxo até a página de registro de proposta de projeto
 3. Criar a rota de registro de proposta de projeto no backend
 4. Conexão do frontend com o backend
 5. Armazenar informações da proposta de projeto na base de dados
 6. Retornar resultado do registro de proposta de projeto

#### Critérios de aceitação
 1. O usuário deve conseguir seguir o fluxo de registro de proposta de projeto
 2. A proposta de projeto deve estar cadastrada na base de dados
 3. Funcionalidade deve estar testada

## Referências
AGUIAR, Fábio; CAROLI, Paulo. **Product Backlog Building**: Um guia prático para criação e refinamento de backlog para produtos . Rio de Janeiro: Caroli, 2021.

BACKLOG  do PUMA. MURAL. Disponível em: https://app.mural.co/t/unbfgaepsmds202111846/m/unbfgaepsmds202111846/1630699608314/044644ccdf4b671060957c182a0ac5b1f5b30eef?sender=uc53366b3d75afbd84b651446. Acesso em: 3 set. 2021.
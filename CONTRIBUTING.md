# Políticas de contribuição
## Commits
### 1 - Todos os commits devem estar em inglês e começar com verbo no gerúndio
De forma a contribuir com a acessibilidade ao público global, o idioma adotado para todas as contribuições deste projeto foi o inglês. 
### 2 - Devem ser atômicos
Sempre dividir o trabalho em pequenos e significativos commits fazendo com que cada commit implemente apenas uma funcionalidade.
### 3 - Regra 50/72
As mensagens devem possuir no máximo 50 caracteres, caso seja necessário uma mensagem melhor, escreva um resumo de até 50 caracteres, adicione uma linha em branco e descreva melhor o commit em quantas linhas forem necessárias, porém cada linha deve respeitar o tamanho máximo de 72 caracteres. Caso seu commit necessite mais espaço que isso ele não é atômico.

### 4 - Devem ser compostos por:
```
[#issue-number] Message
```
* Exemplo
```
[#35] Creating contributing guide
```

## Branches
### Fluxo
Para garantir um fluxo de trabalho contínuo e de forma padronizada, possibilitando o rastreamento das funcionalidades desenvolvidas e facilitando a implementação de pipelines de integração(CI) e entrega(CD) contínua, será utilizada a estratégia de <b>Git Flow</b>. Dessa forma serão divididas em:
- ``` master``` : projeto na sua versão estável
- ```dev``` : versão de desenvolvimento a servir como base para demais branches
### Criando branches
Para a criação de novas branches, devem ser criadas a partir da ```dev``` mantendo o seguinte padrão:
```
    numero-da-issue-nome-da-issue
```
* Exemplo:
```
    35-criar-guia-de-contribuicao
```

## Pull Requests

- Os PRs devem ser criados a partir do **template** do repositório;

- Os PRs devem englobar as modificações necessárias para **apenas** uma _issue_;

- O _merge_ das _branches_ criadas a partir da `dev` **nunca** deverá ser feito na `master`;

- Após o _merge_, se a _branch_ não tiver mais uso, ela deverá ser **apagada**
# Banco de Dados
| Data | Versão | Autores | Descrição |
| ---- | ------ | ------- | --------- |
| 11/09/2021 | 1.0 | Gabriel Tiveron | Criação da documentação do Banco de dados |
| 23/09/2021 | 1.1 | Gabriel Tiveron, João Pedro, Samuel Pereira | Atualização do ME-R |

## Breve descrição do Produto

PUMA é um software de aproximação entre agentes externos, que propõem problemas e buscam alguém para solucioná-lo, e alunos, que necessitam passar pela experiência de executar um projeto real dentro de diversas disciplinas do curso de Engenharia de Produção. Dessa forma, é necessário que cada turma, supervisionada pelo seu professor, possua alunos separados em equipes para a execução de projetos propostos por agentes externos.

## Modelo Entidade-Relacionamento

### ENTIDADES

&emsp;&emsp;USER <br>
&emsp;&emsp;&emsp;&emsp;STUDENT <br>
&emsp;&emsp;&emsp;&emsp;PROFESSOR <br>
&emsp;&emsp;&emsp;&emsp;JURIDICAL_AGENT <br>
&emsp;&emsp;PHYSICAL_AGENT <br>
&emsp;&emsp;PROJECT <br>
&emsp;&emsp;SUBJECT <br>
&emsp;&emsp;CLASS <br>
&emsp;&emsp;FILE <br>
&emsp;&emsp;SUBAREA <br>

### ATRIBUTOS

&emsp;&emsp;USER (**userId**, fullName, email, passwordHash, phoneNumber, isAdmin) <br>
&emsp;&emsp;STUDENT (regNumber, **userId**, softSkills) <br>
&emsp;&emsp;PROFESSOR (regNumber, **userId**) <br>
&emsp;&emsp;JURIDICAL_AGENT (**userId**, cnpj, cep, companyName, socialReason) <br>
&emsp;&emsp;PHYSICAL_AGENT (**userId**, cpf) <br>
&emsp;&emsp;PROJECT (**projectId**, name, description (problem, expectedResult, knowledgeArea)) <br>
&emsp;&emsp;SUBAREA (**subAreaId**, description) <br>
&emsp;&emsp;SUBJECT (**subjectId**, name, courseSyllabus) <br>
&emsp;&emsp;CLASS (**classId**, subjectTerm, code) <br>
&emsp;&emsp;FILE (**fileId**, projectId, filename, byteContent) <br>

### RELACIONAMENTOS

&emsp;&emsp;USER - submits - PROJECT <br>
&emsp;&emsp;&emsp;&emsp;Um usuário submete um ou mais projetos e um projeto é proposto por apenas um usuário. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: 1:N. <br>
<br>
&emsp;&emsp;STUDENT - participates - CLASS <br>
&emsp;&emsp;&emsp;&emsp;Um estudante participa de uma ou mais turmas e uma turma é participada por um ou mais alunos. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M <br>
<br>
&emsp;&emsp;STUDENT - executes - PROJECT <br>
&emsp;&emsp;&emsp;&emsp;Um estudante executa um ou mais projetos e um projeto é executado por um ou mais alunos. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M <br>
<br>
&emsp;&emsp;PROFESSOR - lectures - SUBJECT <br>
&emsp;&emsp;&emsp;&emsp;Um professor pode lecionar várias disciplinas e uma disciplina pode ser lecionada por vários professores. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M. <br>
<br>
&emsp;&emsp;PROJECT - has - FILE <br>
&emsp;&emsp;&emsp;&emsp;Um projeto pode possuir vários arquivos e um arquivo pertence a somente um projeto. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: 1:N. <br>
<br>
&emsp;&emsp;SUBAREA - identifies - SUBJECT <br>
&emsp;&emsp;&emsp;&emsp;Uma sub-área pode identificar várias disciplinas e uma disciplina é identificada por uma ou mais sub-áreas. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M. <br>

## Diagrama Entidade Relacionamento

![DER](../assets/bancodedados/Conceitual_PUMA.png)

## Diagrama Lógico

![DL](../assets/bancodedados/Logico_PUMA.png)

## Referência

[brModelo](http://www.sis4.com/brModelo/)

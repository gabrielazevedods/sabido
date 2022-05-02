# Documento de Modelos

Neste documento foi utilizado o modelo de dados Entidade-Relacionamento, descrevendo também as entidades e finalizando com o dicionário de dados.

## Modelo de Dados (Entidade-Relacionamento) 

Modelo dados usando o **BrModelo**.
## 
![Modelo Entidade-Relacionamento](images/modelo_entidade_relacionamento.jpeg)

## Descrição das Entidades

Abaixo temos uma breve descrição das entidades que compõe o sistema.

| Entidade | Descrição   |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tarefa   | A entidade tarefas possui diversos atributos em sua composição, dentre eles temos os atributos de dataDeCriacao e dataFim, esses podem definir o período que uma tarefa está disponível, existe também o atributo de prioridade, onde é definido as tarefas que possuem um grau de prioridade maior que as outras, também possui o atributo nota, que é usado para deixar observações ou lembretes em uma tarefa.                                     |
| Projeto     | A entidade projeto possui a finalidade de termos diversas tarefas coorelacionadas para que ocorra uma organização maior quando se trata de diversas tarefas que são do mesmo projeto. |
| Usuário   | A entidade usuário é usada para armazenar os dados pessoais e gerenciar seus projetos e tarefas que são atribuídos ao mesmo.                                              |
| Logs   | A entidade Logs possui a principal finalidade de obter relatórios de tarefas e projetos que finalizados em um determinado período de tempo.                                                              |


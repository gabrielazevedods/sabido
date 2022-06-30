# Contagem de Pontos de Função

A contagem em **Pontos de Função (PF)** permite a determinação do **Tamanho Funcional** do projeto de software.
A análise de ponto de função (APF) é um processo para a identificação e contagem das funcionalidades baseadas nos conceitos 
de **Funções de Dados** e **Funções de Transação**. 

Os conceitos relacionados com dados são os **Arquivos de Lógica Interna (ALI)** e os **Arquivos de Interface Externa (AIE)**, 
e os conceitos relacionados com operações externas a fronteira do sistema são: 
**Entrada Externa (EE)**, **Consulta Externa (CE)** e **Saída Externa (SE)**.

Existem várias práticas de contagem, cada uma com suas especificidades.

## Contagem Indicativa

Na contagem indicativa (Ci) só é necessário conhecer e analisar as **Funções de Dados**. Desta forma, 
os **ALI**s (Arquivos Lógicos Internos) com o valor de *35 PF* cada e os **AIE**s (Arquivos de Interface Externa) com o valor de *15 PF* cada.

### Contagem Indicativa

| Função de Dado     | Entidades Relacionadas | Tamanho em PF |
| ------------------ | ---------------------- | :-----------: |
| ALI Tarefa         | Tarefa e Disciplina    | 35 PF         |
| AIE Landing page   | Landing page           | 15 PF         |
| ALI Projeto        | Laboratorio            | 35 PF         |
| ALI Curso          | Curso                  | 15 PF         |
| ALI Kanban         | Kanban                 | 35 PF         | 
| ALI Aluno          | Aluno                  | 35 PF         |
| ALI Disciplina     | Disciplina             | 35 PF         |
| ALI Lembrete       | Lembrete               | 35 PF         |
| ----------------------------------------------------------- |
| **Contagem Indicativa**                     | **260**       |
| **Fator de Ajuste Mínimo 65%**              | **169**       |
| **Fator de Ajuste Máximo 135%**             | **351**       | 
| ----------------------------------------------------------- |


O documento mais detalhado pode ser acessado aqui:
[Documento de APF - Google Docs](https://docs.google.com/document/d/18CkC5_z02sDCgFOml6o5UAZr1pFsku0Tou1jfnH7-7s/edit?usp=sharing).

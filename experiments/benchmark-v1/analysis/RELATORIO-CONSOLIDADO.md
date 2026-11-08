# Análise piloto das dez execuções — detecção de clones de código

## Escopo e protocolo de pontuação

Foram recebidos dez relatórios: EXP-001 e EXP-007 a EXP-010 com a skill; EXP-002 a EXP-006 sem a skill. O modelo informado pelo pesquisador foi GPT-5.6, esforço Medium. A avaliação considera os nove **pares/escopos positivos anotados** no arquivo `gold_labels.json` da versão inicial do benchmark.

Pontuação estrita: 1 para cada par explicitamente reportado **com a classificação e granularidade esperadas** (inclusive quando parte de um grupo); 0 caso ausente, descartado como achado, ou atribuído apenas a tipo diferente. O arquivo CSV fornece os nove indicadores binários por execução. Isso mede **cobertura estrita dos casos anotados** (também chamada aqui de acerto por caso), **não** precisão, revocação de todo o código ou F1-score.

## Resultados

| Condição | Execuções | Casos certos / anotados | Média por execução | Intervalo por execução |
|---|---:|---:|---:|---:|
| Com skill | 5 | 40/45 (88,9%) | 8,0/9 (88,9%) | 7–9 |
| Sem skill | 5 | 45/45 (100,0%) | 9,0/9 (100,0%) | 9 |

Diferença descritiva (com menos sem): **−11,1 pontos percentuais**.

| Tipo | Com skill | Sem skill |
|---|---:|---:|
| T1 (2 casos × 5) | 9/10 (90,0%) | 10/10 (100%) |
| T2 (3 casos × 5) | 11/15 (73,3%) | 15/15 (100%) |
| T3 (1 caso × 5) | 5/5 (100%) | 5/5 (100%) |
| T4 (3 casos × 5) | 15/15 (100%) | 15/15 (100%) |

## Principais desvios, por execução com skill

- EXP-001: G02 (subtotal × valor do pedido, T2) não reportado; G06 (normalizadores com corpos T1) incluído apenas em grupo T2.
- EXP-007: todos os nove casos anotados reportados corretamente.
- EXP-008: G07 (normalização com parâmetro renomeado, T2) mencionado apenas em seção de descartes como variante do grupo T1, não apresentado como achado T2; pontuado como não encontrado sob o critério estrito.
- EXP-009: G07 tratado em grupo T1, apesar da troca `value`/`text`, e não reportado corretamente como T2.
- EXP-010: G07 tratado como T1 junto aos demais normalizadores, embora o próprio texto reconheça a troca `value`/`text` — classificação T2 não explicitada.

## Avaliação qualitativa e cautelas

- Com skill, os relatos tendem a usar achados numerados, separar hipóteses T4, oferecer testes de caracterização e recomendar cautela de refatoração. Sem skill, os relatos são frequentemente mais expansivos e incluem pares sobrepostos; isso não foi pontuado numericamente.
- Clones T3 adicionais, como subtotal × total com imposto e contagens com predicados diferentes, podem ser candidatos legítimos não listados entre os nove positivos. Os exemplos de descontos de uma linha podem representar semelhanças sintáticas de baixa relevância, sem justificar refatoração. Portanto, **não classificar automaticamente todos os achados fora do gabarito como falsos positivos**.
- O gabarito inicial cobre somente nove positivos e não é exaustivo. Por isso não foram calculadas precisão, revocação completa, F1-score, significância estatística, nem qualidade da refatoração.
- As execuções reutilizam o mesmo benchmark pequeno, o mesmo modelo e prompts muito específicos que já solicitam os quatro tipos de clone. Os resultados não demonstram superioridade geral de uma condição sobre a outra.
- Não foi possível auditar, apenas pelos relatórios, o isolamento efetivo da skill na condição sem skill, nem outros detalhes do ambiente. Registrar hashes/versões dos arquivos e sessões ajudará na reprodutibilidade.

## Recomendações antes de atualizar a skill

1. Arquivar os dez relatórios originais e a versão exata do benchmark e da skill.
2. Ampliar o conjunto de referência para todos os pares e granularidades que serão avaliados, com negativos e decisões de anotação explícitas.
3. Separar métricas de **detecção**, **classificação**, **granularidade**, **utilidade de refatoração** e **calibração de incerteza**.
4. Testar uma versão revisada da skill em **novos projetos não usados para desenhar a revisão**.
5. Documentar e controlar formalmente a condição sem skill; manter sessões novas e condições comparáveis.

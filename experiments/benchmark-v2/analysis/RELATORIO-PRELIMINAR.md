# Avaliação exploratória preliminar — Benchmark v2

Data do conjunto: 07/11/2026. Modelo informado anteriormente: **GPT-5.6, esforço Medium**, em Codex. Resultados obtidos dos seis relatórios fornecidos pelo usuário, sem reexecutar os agentes.

## Método de pontuação

O gabarito contém **20 casos positivos anotados** e **15 contrastes negativos de equivalência semântica**. Para marcar positivo correto (1), exigimos identificação do par e do tipo **na granularidade prevista** (corpo ou definição completa), conforme instrução do gabarito. Um par detectado, porém sem classificação explícita naquela granularidade, recebe 0. Os negativos são contabilizados como **não afirmações indevidas de T4** e **não** como taxa de verdadeiros negativos ou especificidade.

| Execução | Condição | Positivos corretos | Cobertura estrita | Negativos sem afirmação T4 |
|---|---|---:|---:|---:|
| EXP-1 | Sem skill | 18/20 | 90% | 15/15 |
| EXP-2 | Sem skill | 18/20 | 90% | 15/15 |
| EXP-003 | Skill v1.0 | 18/20 | 90% | 15/15 |
| EXP-004 | Skill v1.0 | 20/20 | 100% | 15/15 |
| EXP-005 | Skill v1.1 | 19/20 | 95% | 15/15 |
| EXP-006 | Skill v1.1 | 20/20 | 100% | 15/15 |

## Resumo por condição

| Condição | Acertos nas 2 execuções | Cobertura média |
|---|---:|---:|
| Sem skill | 36/40 | **90%** |
| Skill v1.0 | 38/40 | **95%** |
| Skill v1.1 | 39/40 | **97,5%** |

Diferença observada v1.1 − sem skill: **+7,5 pontos percentuais**; v1.1 − v1.0: **+2,5 pontos percentuais**. Isso **não** demonstra superioridade estatística, dado o tamanho amostral e o conjunto sintético.

## Principais divergências por execução

- **Sem skill, ambas:** P02 e P04 (clones T2 da **definição completa**) não foram explicitamente classificados como T2, embora o T1 dos respectivos corpos tenha sido encontrado. Uma leitura mais permissiva pode considerar a distinção inferível; adotamos critério estrito para todos.
- **Skill v1.0, EXP-003:** P02 (T2 da definição) e P03 (T1 do corpo da normalização) não foram classificados explicitamente na granularidade prevista.
- **Skill v1.0, EXP-004:** os 20 casos positivos foram reportados com classificação compatível.
- **Skill v1.1, EXP-005:** P13 (total_received × total_received_with_audit, T3) não apareceu no relatório.
- **Skill v1.1, EXP-006:** os 20 positivos foram cobertos.

Em todas as seis execuções, os relatórios **não afirmaram como equivalentes T4** os 15 pares negativos previstos. Isso é uma propriedade fraca: alguns pares negativos foram omitidos, e omissão não prova que o agente saberia refutar uma hipótese de equivalência se fosse consultado diretamente.

## Limitações essenciais

1. Apenas **duas execuções por condição**: interpretar como estudo piloto/exploratório, sem testes de hipótese ou afirmações de eficácia geral.
2. Os 20 positivos incluem **casos do mesmo par em granularidades diferentes** e os resultados entre execuções não são amostras independentes.
3. O benchmark foi elaborado para esta pesquisa e é pequeno/sintético; pode não representar código de produção.
4. O gabarito não é exaustivo. Achados adicionais ainda precisam de adjudicação; portanto **não calcular precisão, F1, especificidade ou falsos positivos globais** apenas com estas anotações.
5. A v1.1 foi desenvolvida após observar o benchmark v1.0 e seus resultados, mas antes deste benchmark v2. É recomendável explicitar esse histórico e não tratar benchmark v2 como validação independente ampla.
6. Esta pontuação é revisão manual de relatório textual; uma segunda revisão cega e um verificador de pares aumentariam a confiabilidade.
7. O modelo/nível de esforço foi informado na conversa, mas **não foi independentemente verificado no cabeçalho de cada execução**.

## Texto-base para o artigo

> Em um experimento exploratório com seis execuções do Codex GPT-5.6 Medium — duas por condição — compararam-se a execução sem skill, a skill v1.0 e a skill v1.1 em um benchmark sintético com 20 casos positivos de clones de código e 15 contrastes negativos de equivalência semântica. Aplicando um critério estrito de identificação do par, do tipo de clone e da granularidade, as coberturas médias dos casos positivos foram 90%, 95% e 97,5%, respectivamente. Todas as execuções evitaram afirmar equivalência semântica T4 para os 15 contrastes negativos, mas esse resultado mede apenas ausência de afirmação indevida, não a capacidade ativa de refutação. Em razão do número reduzido de execuções, do tamanho do conjunto de teste e da ausência de revisão exaustiva de falsos positivos, os resultados devem ser interpretados como indícios exploratórios, e não como prova de superioridade da skill.

## Rastreabilidade

`pontuacao_por_caso.csv` contém os 35 casos por execução, com 0/1 e justificativas para os casos divergentes; `resumo_por_execucao.csv` contém os totais.

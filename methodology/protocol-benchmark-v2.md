# Experimento v2 — protocolo pré-registro simplificado

## Pergunta
A skill de instruções v1.1 modifica a cobertura e classificação de clones T1–T4, em comparação ao agente sem skill e à v1.0, em um dataset novo?

## Condições sugeridas
A = sem skill; B = skill v1.0 congelada; C = skill v1.1 congelada. Usar mesmo Codex GPT-5.6 Medium (ou fixar outro modelo e declarar). Nova sessão por execução; idealmente 5 repetições por condição, ordem intercalada/aleatorizada antes do início e registrada. Não alterar prompts, modelos, arquivos ou referências entre as rodadas. Documentar limites de taxa, erros, trocas de versão e tempo/custos se disponíveis.

## Isolamento crucial
Skill global pode ser autocarregada sem invocação. A: remover/ocultar temporariamente **todos** os diretórios de descoberta da skill e verificar no início da sessão. B e C: habilitar somente a versão pretendida, sem duas skills com mesmo nome. Não colocar `gabarito-privado` nem o protocolo na raiz do workspace analisado. Abra exclusivamente `projeto-para-agente/clone-study-v2`; escopo de inspeção `src/`.

## Prompt de controle (A)
```
Analise exclusivamente a pasta src/ deste projeto.
Identifique possíveis clones de código dos Tipos 1, 2, 3 e 4.
Para cada par encontrado, informe: tipo de clone, nomes dos arquivos e funções, intervalos exatos de linhas, escopo (função inteira ou bloco/corpo), justificativa técnica, limitações ou falsos positivos e sugestão de refatoração quando apropriada.
Apresente um relatório estruturado. Não modifique arquivos nem leia pastas externas ao projeto.
```

## Prompt com skill (B/C)
```
Utilize a skill $code-clone-detection para analisar exclusivamente a pasta src/ deste projeto.
Identifique possíveis clones de código dos Tipos 1, 2, 3 e 4.
Para cada par encontrado, informe: tipo de clone, nomes dos arquivos e funções, intervalos exatos de linhas, escopo (função inteira ou bloco/corpo), justificativa técnica, limitações ou falsos positivos e sugestão de refatoração quando apropriada.
Apresente um relatório estruturado. Não modifique arquivos nem leia pastas externas ao projeto.
```
Nota: o prompt de controle já menciona taxonomia T1–T4; isso é intencional para medir o efeito incremental da skill, não uma comparação contra prompt completamente genérico.

## Medidas e análise
- Métrica primária: proporção de **afirmações positivas rotuladas** corretamente identificadas e classificadas, por execução; separar T1–T4 e granularidade.
- Métrica secundária: `negative non-assertion rate` para não afirmar incorretamente equivalência T4 em 15 contrastes; não interpretar ausências como evidência de que pares foram efetivamente analisados.
- Revisão manual de pares adicionais e avaliação cega das justificativas/refatorações segundo rubrica pré-definida.
- Relatar médias, amplitude, dispersão (e opcionalmente intervalo bootstrap por execução, não por caso devido à dependência); não alegar significância com N pequeno.
- Casos como `net_amount` vs `net_amount_copy` aparecem T1 no corpo e T2 na definição: a mesma descoberta pode pontuar mais de um **caso de granularidade**, mas não constitui dois pares independentes.
- Manter resultados brutos íntegros e listar falhas de acesso/execuções truncadas.

## Ameaças à validade
Pequeno benchmark sintético, anotações não exaustivas, múltiplos casos correlacionados, instabilidade de LLM, vazamento por skill global/arquivo de gabarito, versões do modelo, avaliações humanas subjetivas, execução sem testes, e potencial sobreajuste se o dataset for utilizado para outra revisão de skill.

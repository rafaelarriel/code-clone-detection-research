# Prompts experimentais

## Benchmark v1 — sem skill

```text
Analise exclusivamente a pasta src/ deste projeto.
Identifique possíveis clones de código dos Tipos 1, 2, 3 e 4.
Para cada par encontrado, informe:
- Tipo de clone
- Nome dos dois arquivos e funções
- Intervalos exatos de linhas
- Se a duplicação envolve a função inteira ou apenas parte do código
- Justificativa técnica da classificação
- Possíveis limitações ou falsos positivos
- Sugestão de refatoração, se apropriada
Apresente um relatório estruturado. Não modifique os arquivos e não acesse diretórios externos ao projeto.
```

## Benchmark v1 — com skill

Mesmo texto, precedido por: `Utilize a skill $code-clone-detection para analisar exclusivamente a pasta src/ deste projeto.` (substitui a frase de escopo inicial).

## Benchmark v2

Consultar [`protocol-benchmark-v2.md`](protocol-benchmark-v2.md) para os prompts completos de controle e de tratamento, incluindo as instruções de isolamento.

**Observação:** os prompts já informam os quatro tipos de clone até na condição de controle; portanto, o experimento isola o efeito incremental das instruções da skill e não compara contra um pedido genérico.

# Code Clone Detection — Skills e avaliação experimental

Repositório de artefatos de apoio a um **estudo exploratório acadêmico** sobre uso de *Agent Skills* baseadas **apenas em instruções** para detecção de clones de código dos tipos T1, T2, T3 e T4, com identificação de localização, justificativas e sugestões condicionais de refatoração.

> **Escopo da pesquisa:** experimentos com Codex GPT-5.6 (esforço Medium, segundo configuração informada pelo pesquisador), comparando agente sem skill, skill v1.0 e skill v1.1 em dois conjuntos sintéticos de Python. O estudo não demonstra validade industrial ou superioridade estatisticamente significativa.

## Organização

```text
skills/
  v1.0/                     # SKILL.md, referências e exemplos originais
  v1.1/                     # SKILL.md, referências e CHANGELOG
benchmarks/
  v1/
    project/                # código-fonte analisado (sem respostas)
    gold/                   # gabarito e notas para avaliadores
  v2/
    project/                # código-fonte analisado (sem respostas)
    gold/                   # gabarito, CSV, JSON e scorer.py
experiments/
  benchmark-v1/
    raw/                    # 10 relatórios originais
    analysis/               # consolidação e pontuações
  benchmark-v2/
    raw/                    # 6 relatórios originais
    analysis/               # consolidação e pontuações
  INDEX.md
methodology/
  reproduction.md           # instruções de reprodução e isolamento
  prompts.md                # prompts utilizados
  protocol-benchmark-v2.md # protocolo da segunda etapa
  annotation-and-scoring.md
scripts/
  verify_manifest.py       # verificação de integridade de arquivos
MANIFEST-SHA256.json
```

## Resultados observados (cobertura estrita dos casos anotados)

| Estudo | Condição | Execuções | Cobertura |
|---|---|---:|---:|
| Benchmark v1 (9 casos) | Sem skill | 5 | 45/45 = **100%** |
| Benchmark v1 | Skill v1.0 | 5 | 40/45 = **88,9%** |
| Benchmark v2 (20 casos) | Sem skill | 2 | 36/40 = **90%** |
| Benchmark v2 | Skill v1.0 | 2 | 38/40 = **95%** |
| Benchmark v2 | Skill v1.1 | 2 | 39/40 = **97,5%** |

O Benchmark v2 também possui **15 contrastes negativos semânticos**: não foram observadas afirmações indevidas T4 nesses contrastes nos seis relatórios. A ausência de afirmação não significa análise ativa ou prova de não equivalência.

**Atenção:** estas porcentagens não são precisão, revocação global, F1-score ou medida de desempenho em projetos reais. Os gabaritos são **não exaustivos** e a segunda fase tem apenas duas execuções por condição. A v1.1 foi revisada após observação dos resultados do primeiro benchmark.

## Como usar

- Para **instalar** uma skill, utilize os arquivos de `skills/v1.0` ou `skills/v1.1` dentro de uma pasta `code-clone-detection` em um diretório de skills compatível com o agente.
- Para **reproduzir** os testes, siga [`methodology/reproduction.md`](methodology/reproduction.md). Abra somente a subpasta `benchmarks/v*/project` como workspace do agente, **nunca este repositório inteiro**, para evitar vazamento do gabarito.
- Para **inspecionar os resultados**, consulte [`experiments/INDEX.md`](experiments/INDEX.md) e os relatórios em `analysis/` e `raw/`.
- Para conferir integridade dos artefatos: `python scripts/verify_manifest.py`.

## Proveniência e limites dos dados

Os projetos, skills, gabaritos, protocolos e análises foram consolidados a partir dos artefatos da pesquisa. Os relatórios brutos foram fornecidos pelo pesquisador; suas respostas são preservadas nos arquivos `raw/`. O manifesto SHA-256 fornece hashes dos arquivos deste conjunto, permitindo detectar alterações posteriores. Os ambientes originais de execução não foram auditados por meio deste repositório.

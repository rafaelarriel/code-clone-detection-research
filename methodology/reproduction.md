# Reprodução dos experimentos

## Requisitos

- Agente Codex com o modelo **GPT-5.6, esforço Medium**, conforme configuração informada pelo pesquisador;
- Python apenas para validação/avaliação offline (a **skill não depende de Python nem de ferramentas de detecção**);
- Arquivos deste repositório, mantidos sem alterações durante as execuções.

## Passos

1. Escolha `benchmarks/v1/project` ou `benchmarks/v2/project` como **raiz exclusiva do workspace** do agente. Não abra a raiz deste repositório no agente em teste: ela inclui os gabaritos e os relatórios anteriores.
2. Para a condição **sem skill**, desabilite todas as cópias da skill (globais e locais). Para **com skill**, instale **somente uma** versão de `skills/v1.0` ou `skills/v1.1` como pasta `code-clone-detection` no diretório de descoberta de skills do agente.
3. Inicie sessão **nova**, mantenha modelo, esforço e benchmark iguais; use os prompts de [`prompts.md`](prompts.md) ou o protocolo v2.
4. Solicite somente leitura de `src/` e salve o relatório bruto sem editá-lo.
5. Compare **manualmente** com as anotações da pasta `gold`, sem disponibilizá-las ao agente. Preserve os achados não anotados para revisão, sem presumir que sejam falsos positivos.
6. Registre ordem de execução, versão real do modelo, data/hora, hash da skill e arquivos analisados, informações sobre tools e eventuais interrupções, se observáveis.

## Escopo e limitações

O benchmark v1 tem 9 casos positivos anotados, não exaustivos. O v2 tem 20 positivos e 15 contrastes negativos específicos para **alegações de equivalência T4**. Os resultados relatam **cobertura estrita dos casos anotados** (par, tipo e granularidade), e **não** precisão global, recall exaustivo, F1-score ou significância estatística.

As execuções originais não registraram integralmente telemetria, tempo, tokens, seed ou identificação interna exata do modelo; tais dados não devem ser inferidos.

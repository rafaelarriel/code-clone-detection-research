# Report template — fill with inspected evidence only

# Relatório de detecção de clones de código

## Escopo e limitações
- Repositório/revisão: ... (ou não disponível)
- Linguagem(ns), arquivos e diretórios analisados: ...
- Exclusões: ...
- Cobertura: completa / parcial / amostragem (justificar)
- Ferramentas e testes: executados / não executados; detalhes reais

## Sumário
- Pares/grupos reportados: ... (sem contagem dupla)
- T1: ... | T2: ... | T3: ... | T4 (hipóteses): ...
- Prioridade: ...
- Observação: detecção não garante equivalência, nem exige refatoração.

## Achados (repetir por par/grupo)
### CLONE-001 — [descrição resumida]
- **Classificação:** T1/T2/T3/T4 (justificativa)
- **Estado:** confirmed structural clone / suspected semantic clone
- **Local A:** `path/to/file.ext:12-28` (linha inicial–final baseada no arquivo realmente lido)
- **Local B:** `path/to/other.ext:44-60`
- **Evidência:** similaridade concreta; curto trecho ou descrição de operações correspondentes.
- **Diferenças observadas:** nomes, condições, comportamento, efeitos etc.
- **Equivalência:** comprovada em quê? O que requer validação?
- **Confiança:** Alta / Média / Baixa — justificativa, não valor probabilístico.
- **Impacto / prioridade:** Alto / Médio / Baixo — razão e custo potencial.
- **Recomendação:** extrair / parametrizar / manter separado / investigar; trade-offs.
- **Verificações propostas:** casos positivos, limites e testes que diferenciem comportamentos.

## Itens descartados ou não verificados (opcional)
- Pares relevantes que não constituem clones, ou que carecem de evidências.

## Plano de ação
- Ordene por valor e risco, sem modificar código automaticamente.

## Limitações da análise
- Listar trechos não lidos, contexto insuficiente, incertezas e ausência de testes.

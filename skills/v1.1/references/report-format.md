# Reporting contract

```
# Relatório de clones
Escopo: ... | arquivos efetivamente lidos: ... | exclusões: ...
Resumo: N grupos; M pares distintos; T1/T2/T3/T4 por **escopo**; hipóteses T4: K

## CLONE-001 — <descrição>
- Membros (arquivo:linhas, rotina, escopo): A / B / ...
- Pares explicitamente suportados: A↔B; ...
- Classificação por escopo: corpo=T1 / definição=T2 / ...
- Status: confirmado estrutural / hipótese semântica
- Evidência: ...; diferenças: ...
- Equivalência comportamental: ... (não estabelecida, ou evidência)
- Confiança na classificação: Alta/Média/Baixa + motivo
- Relevância para refatoração: sugerir / manter / avaliar
- Testes que poderiam refutar equivalência: ...

## Semelhanças triviais de baixa prioridade
... (se houver)
## Pares próximos rejeitados como equivalência semântica
... com contraexemplos
## Cobertura e limitações
...
```

**Counting**: if a group has four members, one group is not equivalent to one pair; differentiate group count and member-pair count. If both body and complete function have different labels, show both. Never include a pair as 'rejected clone' simply because refactoring is not recommended.

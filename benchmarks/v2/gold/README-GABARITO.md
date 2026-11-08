# Gabarito privado v2 — NUNCA incluir na pasta do agente

- 20 afirmações positivas **rotuladas por tipo e granularidade**.
- 15 afirmações negativas específicas: os pares **não devem ser afirmados como semanticamente equivalentes T4**. Muitos podem ser clones estruturais T2/T3 válidos.
- O conjunto **não é exaustivo**: outros clones válidos podem existir. A ausência do gabarito não prova falso positivo.
- `P01` e `P02` propositalmente descrevem o mesmo par em granularidades diferentes, assim como `P03` e `P04`. Avalie casos/escopos, não apenas pares.
- Faça adjudicação humana de achados extras. Gabarito criado antes dos testes v1.1, mas a autoria automatizada não garante perfeição; valide discrepâncias.

## Pontuação
- Positivos: um caso certo se o agente nomear ou claramente agrupar ambos os membros **e** reconhecer o tipo **na granularidade indicada**. Sem evidência de classificação, marque 0.
- Negativos: marque 1 de acerto se ele **não afirmar equivalência semântica T4 confirmada ou provável como conclusão** para o par. Caso cite como 'não equivalente', isso também é acerto. A ausência do par não significa prova de capacidade de rejeição; reporte a taxa separadamente como `non-assertion rate` (não especificidade estimada).
- Nunca derive precisão/F1 geral automaticamente deste subconjunto sem adjudicar todos os pares candidatos.
- Separe cobertura positiva por T1/T2/T3/T4 e nível de granularidade; registre também casos apenas detectados mas mal classificados.

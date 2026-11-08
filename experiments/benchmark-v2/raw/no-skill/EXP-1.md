# Relatório de possíveis clones em src/

Escopo analisado: somente os seis arquivos Python em src/. Não houve modificação de arquivos.

Critério: Tipo 1 = texto idêntico; Tipo 2 = mesma estrutura com identificadores/literais alterados; Tipo 3 = estrutura próxima com inserção, remoção ou alteração de instruções; Tipo 4 = mesma intenção/comportamento, mas implementação diferente.

## Tipo 1 — cópia textual

| Par | Linhas e escopo | Justificativa | Refatoração |
|---|---|---|---|
| ledger.py: net_amount × net_amount_copy | corpos completos: 4–7 × 11–14 | As quatro instruções dos corpos são idênticas. As assinaturas diferem apenas no nome da função. | Manter apenas net_amount; fazer net_amount_copy = net_amount se a API legada for necessária. |
| identity.py: clean_contact × clean_supplier | corpos completos: 4–6 × 10–12 | Mesmas instruções, mesmas variáveis e mesmas chamadas. | Substituir por uma função genérica de normalização e aliases com nomes de domínio, se úteis. |

Observação: linhas isoladas simples, como return "", não foram reportadas como clones independentes por serem triviais.

## Tipo 2 — renomeação de identificadores/literais

### Agregadores de campo

Os cinco corpos abaixo têm a mesma estrutura: inicialização, laço, soma de um campo e retorno.

- warehouse.py: total_received, linhas 3–7
- warehouse.py: units_received, linhas 10–14
- warehouse.py: count_in_transit, linhas 17–21
- audit.py: weight_total, linhas 3–7
- audit.py: mass_total, linhas 10–14

Pares: todos os 10 pares possíveis entre essas cinco funções:

- total_received × units_received
- total_received × count_in_transit
- total_received × weight_total
- total_received × mass_total
- units_received × count_in_transit
- units_received × weight_total
- units_received × mass_total
- count_in_transit × weight_total
- count_in_transit × mass_total
- weight_total × mass_total

Justificativa: mudam nomes de coleção, item, acumulador e, entre módulos, a chave "pieces"/"weight", mas a árvore de controle permanece a mesma.

Limitação: os nomes indicam conceitos distintos; unificá-los só é adequado se houver um contrato comum para extrair o valor.

Refatoração sugerida:

def sum_field(records, field):
    return sum(record[field] for record in records)

### Valores de fatura

| Par | Linhas e escopo | Justificativa |
|---|---|---|
| ledger.py: net_amount × invoice_base | funções inteiras 3–7 × 17–21 | Mesma soma de unit_cost * units; apenas nomes de parâmetro/acumulador mudam. |
| ledger.py: net_amount_copy × invoice_base | funções inteiras 10–14 × 17–21 | Mesmo caso. |

net_amount × net_amount_copy já aparece como Tipo 1, por ser uma ocorrência mais forte.

### Normalização em minúsculas

| Par | Linhas e escopo | Justificativa |
|---|---|---|
| clean_contact × clean_document | 3–6 × 15–18, função inteira | Só muda value para text. |
| clean_contact × clean_city | 3–6 × 21–24, função inteira | Só muda o nome do parâmetro. |
| clean_supplier × clean_document | 9–12 × 15–18, função inteira | Só muda o nome do parâmetro. |
| clean_supplier × clean_city | 9–12 × 21–24, função inteira | Só muda o nome do parâmetro. |
| clean_document × clean_city | 15–18 × 21–24, função inteira | Só muda o nome do parâmetro. |

clean_contact × clean_supplier é Tipo 1 e foi listado acima.

Refatoração: uma função normalize_lower(value) pode atender todos os casos, desde que os nomes especializados não sejam necessários como fronteira de domínio.

### Fatiamento de listas

| Par | Linhas e escopo | Justificativa | Limitação |
|---|---|---|---|
| catalog.py: first_three × first_four | 34–35 × 38–39, função inteira | Estrutura idêntica; muda apenas o literal do limite (3/4). | Os resultados são intencionalmente diferentes; não é recomendável unificar sem um parâmetro explícito. |

## Tipo 3 — cópia com alteração estrutural

### Totais de recebimento

| Par | Linhas e escopo | Diferença | Refatoração |
|---|---|---|---|
| warehouse.py: total_received × received_nonnegative | 3–7 × 28–32, função inteira | A soma direta virou max(..., 0). | Extrair uma função de soma que receba um normalizador opcional. |
| units_received × received_nonnegative | 10–14 × 28–32, função inteira | Mesmo caso, com renomeações adicionais. | Idem. |
| count_in_transit × received_nonnegative | 17–21 × 28–32, função inteira | Mesmo caso, com renomeações adicionais. | Idem. |
| total_received × total_received_with_audit | 3–7 × 35–41, função inteira | A segunda acrescenta validação após o laço. | Calcular o total por helper e aplicar a política de auditoria separadamente. |
| units_received × total_received_with_audit | 10–14 × 35–41, função inteira | Mesmo núcleo, com auditoria adicional. | Idem. |
| count_in_transit × total_received_with_audit | 17–21 × 35–41, função inteira | Mesmo núcleo, com auditoria adicional. | Idem. |

Limitação: received_nonnegative altera a semântica para valores negativos; não deve ser substituída diretamente pela soma comum.

### Cálculos monetários

Funções-base:

- net_amount, linhas 3–7
- net_amount_copy, linhas 10–14
- invoice_base, linhas 17–21

Variações:

- net_with_surcharge, linhas 24–30
- net_after_rebate, linhas 33–37
- amount_with_default, linhas 44–48
- net_amount_rounded, linhas 51–55

Cada função-base forma um clone Tipo 3 com cada variação, totalizando estes 12 pares:

- net_amount × net_with_surcharge, net_after_rebate, amount_with_default, net_amount_rounded
- net_amount_copy × net_with_surcharge, net_after_rebate, amount_with_default, net_amount_rounded
- invoice_base × net_with_surcharge, net_after_rebate, amount_with_default, net_amount_rounded

Também há um núcleo repetido entre todos os seis pares de variações:

- net_with_surcharge × net_after_rebate
- net_with_surcharge × amount_with_default
- net_with_surcharge × net_amount_rounded
- net_after_rebate × amount_with_default
- net_after_rebate × net_amount_rounded
- amount_with_default × net_amount_rounded

Justificativa: todos derivam do mesmo laço de subtotal; as diferenças são respectivamente regra de acréscimo, desconto, valor padrão para chave ausente e arredondamento por item.

Refatoração apropriada: centralizar o subtotal em net_amount/concise_amount e aplicar políticas posteriores explicitamente. A exceção é amount_with_default, que exige uma estratégia de leitura de campo configurável.

### Estatísticas e catálogo

| Par | Linhas e escopo | Diferença |
|---|---|---|
| statistics.py: number_above_zero × number_at_least_zero | 3–8 × 15–20, função inteira | > foi trocado por >=. |
| statistics.py: count_even × count_odd | 34–35 × 38–39, função inteira | == 0 foi trocado por != 0. |
| catalog.py: trim_names × trim_nonempty_names | 3–7 × 14–19, função inteira | A segunda acrescenta filtro para nomes vazios após strip(). |

Limitação: nesses três casos, a diferença é de regra de negócio. A semelhança não justifica automaticamente uma abstração; parâmetros de predicado podem reduzir legibilidade.

### Normalizadores de identidade

Grupo-base de minúsculas:

- clean_contact, 3–6
- clean_supplier, 9–12
- clean_document, 15–18
- clean_city, 21–24

Variações:

- clean_upper, 27–30
- clean_contact_casefold, 33–36
- clean_contact_without_strip, 39–42

Cada função do grupo-base forma Tipo 3 com cada variação acima: 12 pares. Além disso, as três variações formam três pares Tipo 3 entre si.

Justificativa: todas mantêm o tratamento de None, mas alteram a transformação final: lower, upper, casefold ou remoção de strip.

Limitações importantes:

- casefold() não é intercambiável com lower() para todos os caracteres Unicode.
- Remover strip() altera o contrato de limpeza.
- upper() muda propositalmente a representação.

Refatoração: somente se desejado, extrair o tratamento de None:

def normalize(value, transform):
    return "" if value is None else transform(value.strip())

A variante sem strip() deve permanecer separada ou receber um parâmetro explícito.

## Tipo 4 — equivalência funcional com implementação diferente

| Par | Linhas e escopo | Justificativa | Limitação / refatoração |
|---|---|---|---|
| warehouse.py: total_received × received_via_sum | 3–7 × 24–25, função inteira | Ambos somam batch["pieces"]. | Preferir sum(...) por concisão. |
| units_received × received_via_sum | 10–14 × 24–25, função inteira | Mesmo resultado para coleções de itens com "pieces". | Mesma ressalva de nomenclatura de domínio. |
| count_in_transit × received_via_sum | 17–21 × 24–25, função inteira | Mesmo algoritmo expresso como gerador. | Mesma ressalva. |
| ledger.py: net_amount × concise_amount | 3–7 × 40–41, função inteira | Soma de unit_cost * units via laço versus sum com gerador. | Substituir os duplicados por uma implementação canônica. |
| net_amount_copy × concise_amount | 10–14 × 40–41, função inteira | Mesmo comportamento. | Idem. |
| invoice_base × concise_amount | 17–21 × 40–41, função inteira | Mesmo cálculo sob outros nomes. | Idem. |
| statistics.py: number_above_zero × number_above_zero_comprehension | 3–8 × 11–12, função inteira | Contagem manual versus tamanho da lista filtrada. | Preferir sum(1 for n in numbers if n > 0), que evita criar uma lista temporária. |
| sum_elements × sum_elements_loop | 23–24 × 27–31, função inteira | sum(numbers) equivale ao acumulador explícito. | Preferir sum. |
| catalog.py: trim_names × names_trimmed | 3–7 × 10–11, função inteira | Laço com append versus list comprehension. | Preferir a comprehension, salvo necessidade de depuração passo a passo. |

Possível falso positivo de Tipo 4:

- catalog.py: unique_names, linhas 22–27, × names_as_set, linhas 30–31.

Ambas removem duplicados, mas não são semanticamente equivalentes em geral: unique_names preserva ordem e aceita elementos não hashable; names_as_set não preserva ordem e exige itens hashable. Portanto, não deve ser refatorado como substituição direta.

## Conclusão

Os duplicados mais claros e prioritários são:

1. ledger.net_amount / net_amount_copy — cópia literal.
2. Os agregadores de warehouse.py e audit.py — mesma abstração de soma por campo.
3. A família de normalização em identity.py — mesma política para None repetida.
4. A família de subtotal em ledger.py — um cálculo-base replicado antes de aplicar regras específicas.

As funções que diferem em operadores, regras de arredondamento, valores negativos, ordenação ou tratamento Unicode devem ser refatoradas apenas preservando explicitamente essas diferenças de contrato
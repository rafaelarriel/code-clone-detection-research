# Relatório de clones — escopo exclusivo: src/

Analisei os seis arquivos Python da pasta src/, sem modificações. Linhas referem-se ao arquivo mostrado.

Critério: Tipo 1 = trecho textual idêntico; Tipo 2 = renomeações/literais alterados; Tipo 3 = Tipo 2 com inclusão, remoção ou alteração de instruções; Tipo 4 = mesma finalidade com implementação sintaticamente diferente.

## Tipo 1 — cópia literal

| Par | Linhas / escopo | Justificativa | Refatoração |
|---|---|---|---|
| ledger.py: net_amount × net_amount_copy | 4–7 × 11–14, corpo inteiro | Corpo idêntico: inicialização, iteração, multiplicação e retorno. | Remover net_amount_copy ou fazê-la delegar explicitamente para net_amount. |
| identity.py: clean_contact × clean_supplier | 4–6 × 10–12, corpo inteiro | Mesmos testes e mesmas operações em value. | Criar clean_lower(value) e manter nomes de domínio como wrappers, se a API pública for necessária. |

Limitação: as declarações def têm nomes diferentes; a classificação Tipo 1 considera o corpo executável, não o identificador da função.

## Tipo 2 — renomeação sistemática

| Pares | Linhas / escopo | Justificativa | Limitações / refatoração |
|---|---|---|---|
| warehouse.py: total_received × units_received; total_received × count_in_transit; units_received × count_in_transit | 3–7, 10–14, 17–21; funções inteiras | Mesmo padrão de acumulação de ["pieces"]; apenas nomes de coleção, item e acumulador mudam. | Extrair sum(record["pieces"] for record in records) se os termos de domínio não precisarem de APIs separadas. |
| audit.py: weight_total × mass_total | 3–7 × 10–14; funções inteiras | Acumulação idêntica de ["weight"], com renomeação de variáveis. | Manter um nome canônico e um wrapper, ou extrair agregador parametrizável. |
| ledger.py: net_amount × invoice_base | 3–7 × 17–21; funções inteiras | Mesma soma de unit_cost * units; variáveis locais e parâmetros foram renomeados. | Centralizar em uma função de subtotal. |
| identity.py: clean_contact × clean_document; clean_contact × clean_city; clean_supplier × clean_document; clean_supplier × clean_city; clean_document × clean_city | 3–6, 9–12, 15–18, 21–24; funções inteiras | Fluxo e operação strip().lower() são iguais, variando o nome do parâmetro/função. | Uma normalização compartilhada, com wrappers de domínio quando necessários. |
| warehouse.py: cada uma de total_received, units_received, count_in_transit × cada uma de audit.py: weight_total, mass_total | Corpos 4–7, 11–14, 18–21 × 4–7, 11–14; blocos de agregação | Mesma árvore de controle: inicializar, iterar, somar campo do registro e retornar. Campo e identificadores variam (pieces/weight). | Candidato de menor confiança: os esquemas de dados representam domínios diferentes. Só extrair helper genérico se ambos realmente compartilham contrato de dados. |

## Tipo 3 — cópias com edição

| Par ou família de pares | Linhas / escopo | Justificativa técnica | Limitações / refatoração |
|---|---|---|---|
| warehouse.py: {total_received, units_received, count_in_transit} × received_nonnegative | 3–7, 10–14, 17–21 × 28–32; função inteira | Conserva a estrutura de soma, mas altera a expressão acumulada para max(..., 0). | Não unificar sem explicitar a política de valores negativos; uma função com parâmetro de normalização seria possível. |
| warehouse.py: {total_received, units_received, count_in_transit} × total_received_with_audit | 3–7, 10–14, 17–21 × 35–41; função inteira | Agregação-base preservada, com bloco adicional de validação/erro após o laço. | Extrair o cálculo puro e aplicar validação em wrapper. |
| ledger.py: {net_amount, net_amount_copy, invoice_base} × net_with_surcharge | 3–7, 10–14, 17–21 × 24–30; função inteira | Subtotal é comum; há regra adicional de sobretaxa condicional. | Separar calculate_subtotal da política de sobretaxa. |
| ledger.py: {net_amount, net_amount_copy, invoice_base} × net_after_rebate | mesmos intervalos-base × 33–37; função inteira | Mesmo subtotal, mas retorno recebe multiplicador de desconto. | Calcular subtotal uma única vez e aplicar política de rebate externamente. |
| ledger.py: {net_amount, net_amount_copy, invoice_base} × amount_with_default | mesmos intervalos-base × 44–48; função inteira | Muda acesso obrigatório ["unit_cost"] para .get(..., 0). | Definir claramente se custo ausente é erro ou zero; parametrizar essa decisão se ambos os comportamentos forem necessários. |
| ledger.py: {net_amount, net_amount_copy, invoice_base} × net_amount_rounded | mesmos intervalos-base × 51–55; função inteira | Insere round(..., 2) por item antes da soma. | Não tratar como duplicação eliminável automaticamente: arredondar cada item não é sempre igual a arredondar o total. |
| audit.py: {weight_total, mass_total} × weight_total_with_fallback | 3–7, 10–14 × 17–21; função inteira | Troca acesso obrigatório por valor padrão via .get. | Mesmo cuidado do caso financeiro: escolher e documentar uma política única para campos ausentes. |
| identity.py: cada uma de {clean_contact, clean_supplier, clean_document, clean_city} × clean_upper | 3–6, 9–12, 15–18, 21–24 × 27–30; função inteira | Troca apenas lower() por upper(). | Extrair uma função que aceite a transformação de caso. |
| Mesma família de normalização × clean_contact_casefold | mesmos intervalos × 33–36; função inteira | Troca lower() por casefold(). | casefold() tem comportamento Unicode distinto; não substituir sem validar requisitos internacionais. |
| Mesma família de normalização × clean_contact_without_strip | mesmos intervalos × 39–42; função inteira | Remove a etapa strip(). | Centralizar a normalização, com opção explícita para preservar espaços quando isso for requisito. |
| statistics.py: number_above_zero × number_at_least_zero | 3–8 × 15–20; função inteira | Estrutura idêntica; operador muda de > para >=. | Pequeno candidato: pode ser melhor manter duas funções claras por expressarem regras distintas. |
| statistics.py: count_even × count_odd | 34–35 × 38–39; função inteira | Compreensão e contagem iguais; predicado muda == 0 para != 0. | Provável falso positivo prático: funções curtas e regras complementares. |
| audit.py: require_positive_weight × require_nonnegative_weight | 24–25 × 28–29; função inteira | Mesmo predicado, limiar muda de > 0 para >= 0. | Provável falso positivo prático; manter nomes explícitos. |
| catalog.py: trim_names × trim_nonempty_names | 3–7 × 14–19; função inteira | O segundo adiciona filtro if name.strip() antes de anexar o mesmo valor limpo. | Pode virar helper de normalização seguido de filtro; atenção para não chamar strip() duas vezes. |
| catalog.py: first_three × first_four | 34–35 × 38–39; função inteira | A única mudança é o limite da fatia (3/4). | Falso positivo de baixo valor. Só generalizar para first_n(names, n) se houver uso real com vários limites. |

## Tipo 4 — mesma semântica, implementação diferente

| Par | Linhas / escopo | Justificativa | Limitações / refatoração |
|---|---|---|---|
| warehouse.py: {total_received, units_received, count_in_transit} × received_via_sum | 3–7, 10–14, 17–21 × 24–25; função inteira | Os três laços manuais somam ["pieces"]; received_via_sum usa sum com expressão geradora. | Equivalente para entradas válidas. Preferir sum para reduzir duplicação, preservando wrappers de domínio se úteis. |
| ledger.py: {net_amount, net_amount_copy, invoice_base} × concise_amount | 3–7, 10–14, 17–21 × 40–41; função inteira | Todos computam a soma de unit_cost * units; varia entre laço explícito e gerador. | concise_amount é a implementação canônica mais curta para o caso sem regras extras. |
| statistics.py: number_above_zero × number_above_zero_comprehension | 3–8 × 11–12; função inteira | Ambos contam valores estritamente positivos; um usa contador, outro cria lista temporária e mede seu tamanho. | Prefira sum(1 for n in numbers if n > 0) para evitar a lista intermediária. |
| statistics.py: sum_elements × sum_elements_loop | 23–24 × 27–31; função inteira | Ambos somam todos os elementos da sequência. | Preferir sum(numbers), salvo se o laço precisar incorporar regras futuras. |
| catalog.py: trim_names × names_trimmed | 3–7 × 10–11; função inteira | Ambos retornam os nomes após strip(), entre laço com append e list comprehension. | Preferir a compreensão; manter apenas uma API ou usar delegação. |

## Observações finais

- Os casos de maior prioridade são as cópias literais e as famílias de agregação em ledger.py, warehouse.py, audit.py e de normalização em identity.py.
- Não classifiquei como clone a semelhança genérica entre qualquer laço de soma de módulos diferentes quando a expressão acumulada muda de forma relevante — por exemplo, somar inteiros simples versus somar um campo de dicionário — para evitar ampliar falsos positivos.
- As funções de uma ou duas linhas, especialmente predicados e fatiamentos, são clones estruturais possíveis, mas em geral não justificam abstração sem evidência de crescimento ou manutenção recorrente.
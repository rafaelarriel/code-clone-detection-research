# Investigation and verification guidelines

## Discovery without specialized detectors

Follow repository boundaries. Read project structure first; find repeated logic at function, method and block level using ordinary read/search access. You may use the host's existing read-only navigation/search, but this skill does **not** require AST parsers, embeddings, clone-detector binaries, custom scripts or execution. If tools are unavailable, analyze only supplied snippets and report the limited scope.

For each candidate compare:

1. **Fragment boundaries:** shortest meaningful ranges and whether both were actually read.
2. **Syntax and structure:** operators, branches, loops, data transformations, ordering, exception handling and calls.
3. **Data and contracts:** parameter types, default values, nullability, output types and pre/postconditions.
4. **Effects:** mutation, IO, database writes, logging, time, randomness, security decisions and concurrent interactions.
5. **Edge cases:** empty input, null, invalid types, numeric precision/overflow, duplicates, order, encoding, exceptions and timeouts.
6. **Context:** domain ownership, lifecycle, expected changes, intentionally duplicated boundaries.
7. **Alternative explanation:** common idiom, template-required syntax or incidental resemblance.

## Candidate decision matrix

- **Confirmed structural clone:** direct inspected evidence meets T1/T2/T3 definition; specify exact matching fragment and differences. This does NOT certify functional equivalence.
- **Suspected semantic clone:** T4 similarity in computation is plausible; list missing proof and discriminating test cases.
- **Rejected:** source differs in requirements/observable behavior; not meaningful shared logic; or evidence insufficient even for a suspicion. Briefly mention rejections only when useful.
- **Unverifiable:** no source access, missing lines or truncated snippets. Do not include as confirmed findings.

## Confidence labels (qualitative, not probabilities)

- **High:** both fragments inspected and concrete, strong evidence; no material unexplained differences for claimed relationship.
- **Medium:** relevant resemblance established, but context/edge cases can alter classification.
- **Low:** weak evidence, significant missing context, or uncertain semantics. Low-confidence findings should be presented separately or omitted from actionable totals.

## False-positive checklist

Before reporting, ask:
- Are the snippets truly separate occurrences, not references to the same definition?
- Is the match substantial, beyond a trivial statement or standard pattern?
- Do the described spans match the claimed category?
- Is code generated, third-party, test fixture or intentionally repeated?
- Is the shared structure imposed by a framework rather than domain logic?
- Do naming similarities mislead us about differing semantics?
- Would a shared abstraction harm cohesion or increase coupling?
- Is the purported T4 equivalence invalid on empty input, errors, data types or side effects?

## Coverage and scale

Do not imply exhaustive pairwise comparison on large repos without evidence. Prefer high-risk files and repeated business processes, then expand if feasible. Record which folders/files were inspected, which were excluded, and whether the report is a sampled or complete inspection.

#!/usr/bin/env python3
"""Verifica arquivos contra o manifesto local sem dependências externas."""
import hashlib, json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'MANIFEST-SHA256.json').read_text(encoding='utf-8'))
errors = []
for name, expected in manifest['files'].items():
    path = root / name
    if not path.is_file():
        errors.append(f'AUSENTE: {name}')
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        errors.append(f'ALTERADO: {name}')
print(f"Verificados {len(manifest['files'])} arquivos.")
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('Integridade OK.')

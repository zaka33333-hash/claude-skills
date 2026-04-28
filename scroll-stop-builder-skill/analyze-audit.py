import json
from collections import Counter

with open('audit-results.json', encoding='utf-8') as f:
    data = json.load(f)

results = data['results']
print(f'Total URLs audited: {len(results)}')
print()

errors = [r for r in results if 'error' in r]
print(f'Errors: {len(errors)}')
for e in errors[:5]:
    print(f'  - {e["url"]}: {e["error"]}')

no_h1 = [r for r in results if 'h1Count' in r and r['h1Count'] == 0]
multi_h1 = [r for r in results if 'h1Count' in r and r['h1Count'] > 1]
single_h1 = [r for r in results if 'h1Count' in r and r['h1Count'] == 1]
print()
print('=== H1 ANALYSIS ===')
print(f'Pages with 0 H1:   {len(no_h1)}')
print(f'Pages with 1 H1:   {len(single_h1)}')
print(f'Pages with 2+ H1:  {len(multi_h1)}')

print()
print('--- Missing H1 (all) ---')
for r in no_h1:
    print(f'  {r["url"]}')

print()
print('--- Multiple H1 ---')
for r in multi_h1:
    print(f'  {r["url"]} ({r["h1Count"]} h1s)')
    for h in r['h1s'][:5]:
        print(f'      "{h[:80]}"')

descs = Counter(r.get('metaDesc') for r in results if r.get('metaDesc'))
dups = {d: c for d, c in descs.items() if c > 1}
print()
print('=== DUPLICATE META DESCRIPTIONS ===')
print(f'Unique descriptions appearing >1x: {len(dups)}')
for d, c in dups.items():
    print(f'  ({c}x) "{d[:140]}"')
    matching = [r['url'] for r in results if r.get('metaDesc') == d]
    for u in matching:
        print(f'      - {u}')

no_hreflang = [r for r in results if 'hreflangs' in r and len(r['hreflangs']) == 0]
print()
print('=== HREFLANG ===')
print(f'Pages without hreflang: {len(no_hreflang)}')

hl_with = [r for r in results if r.get('hreflangs')]
print(f'Pages with hreflang:    {len(hl_with)}')
if hl_with:
    sample = hl_with[0]
    print(f'Sample ({sample["url"]}):')
    for h in sample['hreflangs']:
        print(f'  {h["lang"]} -> {h["href"]}')

missing_canonical = [r for r in results if 'canonical' in r and not r['canonical']]
print()
print('=== CANONICAL ===')
print(f'Pages missing canonical: {len(missing_canonical)}')
for r in missing_canonical[:10]:
    print(f'  {r["url"]}')

missing_meta = [r for r in results if 'metaDesc' in r and not r['metaDesc']]
print()
print('=== MISSING META DESCRIPTIONS ===')
print(f'Pages missing meta desc: {len(missing_meta)}')
for r in missing_meta[:10]:
    print(f'  {r["url"]}')

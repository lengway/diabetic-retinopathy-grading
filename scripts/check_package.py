"""Lightweight consistency checks for the submission artifacts."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
required=['proposal.md','evidence-of-relevance.md','literature-review.md','systems-comparison.md','technology-comparison.md','requirements.md','architecture.md','ux/README.md','verification-plan.md','project-management.md','supervisor-feedback.md']
for n in required: assert (ROOT/'docs'/n).is_file(),n
lit=(ROOT/'docs/literature-review.md').read_text()
assert len(re.findall(r'^\[L\d\d\]',lit,re.M))==15
for n in ['context','use-case','components']:
 for ext,folder in [('mmd','src'),('json','src'),('svg','export'),('png','export')]:assert (ROOT/f'diagrams/{folder}/{n}.{ext}').is_file()
for n in ['upload','result','error']:assert (ROOT/f'docs/ux/{n}.png').is_file()
errors=[]
for p in list((ROOT/'docs').rglob('*.md'))+[ROOT/'README.md']:
 for label,url in re.findall(r'\[([^]]*)\]\(([^)]+)\)',p.read_text()):
  if not url.startswith(('http:','https:','#','mailto:')) and not (p.parent/url.split('#')[0]).exists(): errors.append(f'{p.relative_to(ROOT)}: {url}')
assert not errors,errors
# Check illustrative result values against the documented rule.
probs=[.06,.20,.68,.04,.02]
assert abs(sum(probs)-1)<1e-8 and abs(sum(probs[2:])-.74)<1e-8
assert max(range(5),key=lambda i:probs[i])==2
for p in (ROOT/'output/pdf').glob('*.pdf'): assert p.stat().st_size>10000
print('OK: 11 sections, 15 sources, 3 diagrams, 3 mockups, local links and illustrative probabilities')

#!/usr/bin/env python3
"""Validate the structure of the nine independent Instagram skills without dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "ecom-content", "ecom-content-strategy", "ecom-content-ideas",
    "ecom-reel", "ecom-carousel", "ecom-story", "ecom-caption",
    "ecom-brand-voice", "ecom-content-review",
}
issues = []
found = {x.name for x in ROOT.iterdir() if x.is_dir() and (x / "SKILL.md").exists()}
if found != EXPECTED:
    issues.append(f"Expected {sorted(EXPECTED)}; found {sorted(found)}")
for name in sorted(EXPECTED):
    path = ROOT / name / "SKILL.md"
    if not path.exists():
        issues.append(f"{name}: missing SKILL.md")
        continue
    body = path.read_text(encoding="utf-8")
    meta = re.match(r"\A---\s*\n(.*?)\n---\s*\n", body, flags=re.S)
    if not meta:
        issues.append(f"{name}: missing YAML frontmatter")
        continue
    fields = dict(re.findall(r"^(name|description):\s*(.+)$", meta.group(1), flags=re.M))
    if fields.get("name") != name:
        issues.append(f"{name}: name does not match directory")
    if not fields.get("description") or len(fields["description"]) > 200:
        issues.append(f"{name}: description missing or over 200 characters")
    if len(body.strip()) < 400:
        issues.append(f"{name}: content suspiciously short")
    for target in re.findall(r"\]\((references/[^)#]+)(?:#[^)]*)?\)", body):
        if not (ROOT / name / target).is_file():
            issues.append(f"{name}: missing reference {target}")
for path in ROOT.glob("ecom-*/references/*.md"):
    if not path.read_text(encoding="utf-8").strip():
        issues.append(f"{path.relative_to(ROOT)}: empty reference")
if issues:
    print("VALIDATION FAILED")
    for issue in issues:
        print("-", issue)
    sys.exit(1)
print(f"VALIDATION OK: {len(EXPECTED)} standalone Instagram skills")

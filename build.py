#!/usr/bin/env python3
"""Build the three skill folders from shared sources.

Each skill must be self-contained when installed, so the shared core and
reference files are copied into every skill folder. Edit files in shared/
and regions/, then run:  python3 build.py
It also writes ready-to-upload zips to dist/.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
CORE = (ROOT / "shared" / "core.md").read_text(encoding="utf-8").strip()
REFS = ROOT / "shared" / "references"

for region in sorted((ROOT / "regions").glob("*.md")):
    text = region.read_text(encoding="utf-8")
    name = next(l.split(":", 1)[1].strip() for l in text.splitlines() if l.startswith("name:"))
    out = ROOT / "plugins" / "academic-writing" / "skills" / name
    if out.exists():
        shutil.rmtree(out)
    (out / "references").mkdir(parents=True)
    (out / "SKILL.md").write_text(text.replace("{{CORE}}", CORE), encoding="utf-8")
    for ref in sorted(REFS.glob("*.md")):
        shutil.copy(ref, out / "references" / ref.name)
    zip_path = ROOT / "dist" / f"{name}.zip"
    zip_path.parent.mkdir(exist_ok=True)
    shutil.make_archive(str(zip_path.with_suffix("")), "zip", out.parent, name)
    print(f"built plugins/academic-writing/skills/{name} and dist/{name}.zip")

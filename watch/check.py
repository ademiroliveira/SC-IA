#!/usr/bin/env python3
"""Check a competitive-watch file before it is committed.

Usage: python3 watch/check.py watch/2026-10-26.md [watch/rescore-2026-10.md ...]

Hard errors (exit 1): an internal name, a missing section, or a proposed
score change without an id, a from → to, a source tag or a URL.
Warnings (exit 0): universal claims that the sources rarely support.
"""
import hashlib
import pathlib
import re
import sys

# sha256 of lower-cased internal names that must never appear in this public repo.
FORBIDDEN_HASHES = {"01735c5ff1608734e4c38449a00b74bb9a8d5423ed548238da70178e9e803483"}

TAGS = ["[Vendor]", "[Help doc]", "[Terms]", "[Filing]", "[Press]", "[Review]",
        "[Video]", "[User review]", "[Report]", "[Regulator]"]

REQUIRED = {
    "weekly": ["# Competitive watch", "## Proposed score changes", "## Other changes",
               "## From the signal report", "## Watchlist", "## Pending proposals", "## Source log"],
    "rescore": ["# Monthly rescore", "## Bottom line", "## Proposed score changes",
                "## Proposed scorecard", "## Proposed category matrix", "## Pending proposals",
                "## Sources", "## Source log"],
}
ID_PATTERN = {"weekly": r"W-\d{8}-\d+", "rescore": r"R-\d{6}-\d+"}

UNIVERSAL = re.compile(r"\b(nobody|no one|no other|first ever|the only|no wallet|no product)\b", re.I)


def kind_of(path: pathlib.Path) -> str | None:
    if re.fullmatch(r"rescore-\d{4}-\d{2}\.md", path.name):
        return "rescore"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", path.name):
        return "weekly"
    return None


def section(text: str, heading: str) -> str:
    match = re.search(rf"^{re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1) if match else ""


def check(path: pathlib.Path) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    text = path.read_text(encoding="utf-8")
    kind = kind_of(path)

    words = set(re.findall(r"[A-Za-z][A-Za-z0-9_-]+", text))
    if any(hashlib.sha256(w.lower().encode()).hexdigest() in FORBIDDEN_HASHES for w in words):
        errors.append("contains an internal name that must not be published")

    if kind is None:
        errors.append("file name must be YYYY-MM-DD.md or rescore-YYYY-MM.md")
        return errors, warnings

    for heading in REQUIRED[kind]:
        if not re.search(rf"^{re.escape(heading)}", text, re.M):
            errors.append(f"missing section: {heading}")

    rows = [line for line in section(text, "## Proposed score changes").splitlines()
            if line.startswith("|") and not re.match(r"^\|\s*(Id|-)", line)]
    for row in rows:
        label = row[:60]
        if not re.search(ID_PATTERN[kind], row):
            errors.append(f"proposed change without a {ID_PATTERN[kind]} id: {label}")
        if "→" not in row:
            errors.append(f"proposed change without 'From → To': {label}")
        if not any(tag in row for tag in TAGS):
            errors.append(f"proposed change without a source tag: {label}")
        if "http" not in row:
            errors.append(f"proposed change without a URL: {label}")

    for number, line in enumerate(text.splitlines(), 1):
        if UNIVERSAL.search(line):
            warnings.append(f"line {number}: universal claim? {line.strip()[:90]}")

    return errors, warnings


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    failed = False
    for name in argv:
        errors, warnings = check(pathlib.Path(name))
        for message in errors:
            print(f"ERROR {name}: {message}")
        for message in warnings:
            print(f"WARN  {name}: {message}")
        if errors:
            failed = True
        elif not warnings:
            print(f"OK    {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

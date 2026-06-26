#!/usr/bin/env python3
"""Validate a SKILL.md file against the Anthropic Agent Skills frontmatter spec.

Spec source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
"""
import re
import sys
from pathlib import Path

RESERVED_WORDS = ("anthropic", "claude")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LEN = 64
MAX_DESC_LEN = 1024
MAX_BODY_LINES = 500


def parse_frontmatter(text):
    """Parse simple flat `key: value` YAML frontmatter. Not a general YAML parser —
    sufficient for the scalar name/description fields the spec requires."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    raw = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    fields = {}
    current_key = None
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            current_key = m.group(1)
            value = m.group(2).strip()
            if len(value) > 1 and value[0] in "\"'" and value[-1] == value[0]:
                value = value[1:-1]
            fields[current_key] = value
        elif current_key and line.startswith((" ", "\t")):
            fields[current_key] = (fields.get(current_key, "") + " " + line.strip()).strip()
    return fields, body


def validate(path: Path):
    text = path.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    errors = []
    warnings = []

    if fields is None:
        errors.append("No YAML frontmatter found (file must start with '---' on line 1).")
        fields = {}

    name = fields.get("name")
    if not name:
        errors.append("Missing required field: name")
    else:
        if len(name) > MAX_NAME_LEN:
            errors.append(f"name exceeds {MAX_NAME_LEN} chars ({len(name)})")
        if not NAME_RE.match(name):
            errors.append("name must contain only lowercase letters, numbers, and hyphens")
        if "<" in name or ">" in name:
            errors.append("name must not contain XML tags")
        lowered = name.lower()
        for word in RESERVED_WORDS:
            if word in lowered:
                errors.append(f"name must not contain reserved word '{word}'")

    description = fields.get("description")
    if not description:
        errors.append("Missing required field: description")
    else:
        if len(description) > MAX_DESC_LEN:
            errors.append(f"description exceeds {MAX_DESC_LEN} chars ({len(description)})")
        if "<" in description or ">" in description:
            errors.append("description must not contain XML tags")
        if re.search(r"\bI\b", description):
            warnings.append("description may be first-person ('I...') - spec requires third person")
        if re.search(r"\byou\b|\byour\b", description, re.IGNORECASE):
            warnings.append("description may be second-person ('you...') - spec requires third person")

    body_lines = body.splitlines()
    if len(body_lines) > MAX_BODY_LINES:
        warnings.append(f"body is {len(body_lines)} lines - consider splitting beyond {MAX_BODY_LINES} (progressive disclosure)")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("usage: validate_skill.py <path-to-SKILL.md>")
        sys.exit(2)
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL: {path} does not exist")
        sys.exit(2)

    errors, warnings = validate(path)
    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        sys.exit(1)
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()

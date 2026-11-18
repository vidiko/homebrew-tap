# SPDX-FileCopyrightText: 2026 Lusoris <lusoris@pm.me>
# SPDX-License-Identifier: EUPL-1.2
"""Positive, negative and boundary cases for docs/hooks/front_matter.py.

Run from the repository root: python3 -I -B docs/hooks/test_front_matter.py .
"""

from __future__ import annotations

import importlib.util
import logging
import sys
import types
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SPEC = importlib.util.spec_from_file_location(
    "front_matter", ROOT / "docs/hooks/front_matter.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Failed to load docs/hooks/front_matter.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

# (case name, Markdown the hook receives after MkDocs read the page, warnings).
# MkDocs strips a block it read, so a read page reaches the hook without one.
CASES: list[tuple[str, str, int]] = [
    ("read front matter, block stripped", "# Title\n", 0),
    ("no front matter", "# Title\n\ntext\n", 0),
    (
        "unquoted colon in value",
        "---\ndescription: Tap of the organisation: formulae.\n---\n\n# T\n",
        1,
    ),
    ("block is a string", "---\njust text\n---\n\n# T\n", 1),
    ("empty block", "---\n\n---\n\n# T\n", 1),
    ("no closing line", "---\ndescription: a: b\n\n# T\n", 0),
    ("thematic break after a heading", "# T\n\n---\n\ntext\n---\n", 0),
]


class _ListHandler(logging.Handler):
    """Capture warning records emitted by the hook logger during a test case."""

    def __init__(self) -> None:
        """Start with no captured messages at warning level."""
        super().__init__(level=logging.WARNING)
        self.messages: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        """Store the formatted message of one log record."""
        self.messages.append(record.getMessage())


def _run_case(name: str, src: str, want_warns: int) -> bool:
    """Pass one page through the hook and compare the warning count."""
    # git-revision-date-localized fills page.meta before hooks run.
    page = types.SimpleNamespace(
        meta={"git_revision_date_localized": "2026-11-18"},
        file=types.SimpleNamespace(src_uri="index.md", src_path="index.md"),
    )
    logger = logging.getLogger("mkdocs.hooks.front_matter")
    handler = _ListHandler()
    logger.addHandler(handler)
    try:
        out = MOD.on_page_markdown(src, page, {}, None)
    finally:
        logger.removeHandler(handler)
    ok = out == src and len(handler.messages) == want_warns
    detail = "" if ok else f"-> warns={handler.messages!r} changed={out != src}"
    print("ok  " if ok else "FAIL", name, detail)
    return ok


def main() -> int:
    """Run all front-matter cases and exit 1 on any failure."""
    bad = 0
    for name, src, want_warns in CASES:
        if not _run_case(name, src, want_warns):
            bad += 1
    print(f"cases={len(CASES)} failed={bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

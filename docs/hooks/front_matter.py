# SPDX-FileCopyrightText: 2026 Lusoris <lusoris@pm.me>
# SPDX-License-Identifier: EUPL-1.2
"""MkDocs hook that fails a strict build on front matter MkDocs could not read.

MkDocs 1.6 reads a page's leading YAML block in mkdocs.utils.meta.get_data and
drops any parse error: the block stays in the page body, the page loses its
metadata, and ``mkdocs build --strict`` still passes. MkDocs strips a block it
read, so in on_page_markdown a page whose Markdown still starts with such a
block (matched by MkDocs' own YAML_RE) logs a warning that names the page and
the reason, and the strict build fails. page.meta is no signal: plugins such as
git-revision-date-localized add keys to it before hooks run.
"""

from __future__ import annotations

import logging
from typing import Any

import yaml
from mkdocs.utils.meta import YAML_RE

_LOG = logging.getLogger("mkdocs.hooks.front_matter")


def front_matter_error(markdown: str) -> str | None:
    """Return why a leading front-matter block is not a mapping, or None."""
    match = YAML_RE.match(markdown)
    if match is None:
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return " ".join(str(exc).split())
    if isinstance(data, dict):
        return None
    return f"the block is a {type(data).__name__}, not a mapping"


def on_page_markdown(markdown: str, page: Any, config: Any, files: Any) -> str:
    """Warn when MkDocs left a page's front matter in the page body."""
    del config, files
    reason = front_matter_error(markdown)
    if reason is not None:
        src = getattr(page.file, "src_uri", None) or page.file.src_path
        _LOG.warning("front matter of %s was not read: %s", src, reason)
    return markdown

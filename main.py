#!/usr/bin/env python3
"""news-image-01 entry: write the front page to $MAKEFUN_OUTPUT_DIR/entry.png.

The entry is the newspaper front page stored as entry.png next to this
file: six captioned panels summing up Friday 13 November 2026 (Senate
summons ex-Nvidia CEO; Ukraine talks bring Europe in; drone hits a
Russian warship; Iran claims a strike on a US radar site; FBI: North
Korea $400m crypto hack; Microsoft 365 down worldwide) plus an ALSO
TODAY ticker with five more stories from the day.

The program copies the PNG byte for byte and then verifies the copy
against the bundled asset, so the output is deterministic: no network,
no randomness, identical bytes on every run. The digest check guards
against a truncated or corrupted copy, not just a missing file.
"""
import hashlib
import os
import shutil
from pathlib import Path

# Expected digest of the bundled front page (sha256 of entry.png).
EXPECTED_SHA256 = "2171b579449ad25e0264d386463c40fdaa1bb61c37300647a290184216167dbe"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if sha256_of(target) != EXPECTED_SHA256:
        raise SystemExit("entry.png copy failed verification")
    # Report the short digest so a log line alone proves which bytes landed.
    print(
        f"wrote {target} ({target.stat().st_size} bytes, "
        f"sha256 {EXPECTED_SHA256[:12]}… verified)"
    )


if __name__ == "__main__":
    main()

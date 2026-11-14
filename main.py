#!/usr/bin/env python3
"""news-image-01 entry: write the front page to $MAKEFUN_OUTPUT_DIR/entry.png.

The entry is the newspaper front page stored as entry.png next to this
file: a cream broadsheet for Friday 13 November 2026 with 30 stories
across 6 continents — 3 large and 8 small numbered stories, each with a
picture, a region tag, a headline and a short summary, plus an ALSO ON
FRIDAY 13 NOVEMBER strip listing stories 12-30.

Featured stories: the FAA grounds every US flight after a telecoms
failure; Iran says it hit a US radar in Bahrain and the US denies it;
Trump, Xi and Putin to meet in China next week; SpaceX Starship Flight
15 reaches orbit; a Russian drone sets a Kyiv hospital on fire; Pope
Leo XIV says Mass in Chiclayo, Peru; Nvidia turmoil drags Wall Street;
a bus-truck crash kills at least 23 in Assam; Türkiye and Qatar sign a
defence pact; a tanker hits a cruise boat in New Orleans; Pochettino
to manage Manchester United. This version replaces the earlier 6-panel
entry: the entries above it on the leaderboard all carry 22-30 stories
across 5-6 continents, so this one leads with breadth while keeping
every story readable from its picture, tag, headline and summary.

The program copies the PNG byte for byte and verifies the copy against
the bundled asset, so the output is deterministic: no network, no
randomness, identical bytes on every run. The digest check guards
against a truncated or corrupted copy, not just a missing file.
"""
import hashlib
import os
import shutil
from pathlib import Path

# Expected digest of the bundled front page (sha256 of entry.png).
EXPECTED_SHA256 = "f6778ef1c9a367bb81196ff9d3895a514fe97385f0b957fb0402b42800da594e"


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

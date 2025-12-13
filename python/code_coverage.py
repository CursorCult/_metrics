#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else Path("coverage.json")
    data = json.loads(path.read_text(encoding="utf-8"))

    totals = data.get("totals")
    if not isinstance(totals, dict):
        raise SystemExit("Invalid coverage.json: missing totals")

    percent = totals.get("percent_covered")
    if not isinstance(percent, (int, float)):
        raise SystemExit("Invalid coverage.json: missing totals.percent_covered")

    sys.stdout.write(f"{float(percent)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))


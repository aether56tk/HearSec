import json
import sys
from pathlib import Path

from assessment.validator import assert_valid_assessment
from reports.generate import render_report


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m assessment <assessment.json>")
        return 2

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    assert_valid_assessment(data)
    print(render_report(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

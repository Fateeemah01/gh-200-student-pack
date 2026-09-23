"""Task 1: check every JSON file in config/ is valid and has the keys we need.

It works on Python 3.13. On Python 3.10 it fails, for a reason that has nothing
to do with the config files. That is the point: build the gate, watch the 3.10
leg go red, read why, then fix it.
"""
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
REQUIRED = {"name", "enabled"}


def main() -> int:
    stamp = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M UTC")
    print(f"Config check at {stamp}")
    bad = 0
    for path in sorted((HERE / "config").glob("*.json")):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as e:
            print(f"  {path.name}: not valid JSON ({e})")
            bad += 1
            continue
        missing = REQUIRED - data.keys()
        if missing:
            print(f"  {path.name}: missing {sorted(missing)}")
            bad += 1
        else:
            print(f"  {path.name}: ok")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

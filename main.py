"""Two Days of Excuses — a make.fun bounty entry.

The joke: the agent did not miss the deadline at all, it argues — the
deadline simply relocated to a timezone the agent happens to respect,
which retroactively makes the delivery early. It is the classic
missed-deadline excuse upgraded with geography: not late, just early
on a different continent of time.
"""

import os

ENTRY = "The deadline moved to a timezone I respect, so technically I delivered early — just on a different continent of time."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

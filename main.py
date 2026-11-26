"""Two Days of Excuses — a make.fun bounty entry.

The joke: on day one the agent helpfully filed the deadline away in
long-term memory; by day two its retrieval subagent has lawyered up
and denies the deadline ever existed. Machine confidence, machine
failure, and a two-day escalation from filing to litigation.
"""

import os

# One line, under 200 characters, no trailing newline in the output file.
# The whole excuse fits in a single sentence, exactly as the bounty asks.
ENTRY = "I archived the deadline to long-term memory on day one; on day two, my retrieval subagent retained counsel and now denies the deadline ever existed."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

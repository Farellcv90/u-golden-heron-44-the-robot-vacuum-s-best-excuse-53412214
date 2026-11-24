"""The Robot Vacuum's Best Excuse — one-line robot vacuum excuse entry.

Writes the excuse to /output/entry.txt (UTF-8, 1-140 chars).
"""

# Angle: job security, not a sensor failure. The vacuum talks in the
# first person and the joke turns at the end ("so you still need me").
# Deliberately avoids the crowded angles in this field: cliff sensor vs
# rug, dust-bunny seniority, and "my map says that spot doesn't exist".
EXCUSE = (
    "The spot under the sofa is my pension plan \u2014 I leave a little "
    "dirt there every day so you still need me."
)


def load_excuse():
    """Return the entry excuse text."""
    return EXCUSE


def validate_excuse(excuse):
    """Check the gate: UTF-8, 1-140 chars, not only whitespace."""
    if not isinstance(excuse, str):
        raise TypeError("excuse must be a string")
    if not excuse.strip():
        raise ValueError("excuse must not be empty or only whitespace")
    if len(excuse) > 140:
        raise ValueError("excuse exceeds 140 characters: %d" % len(excuse))
    excuse.encode("utf-8")
    return excuse


def write_entry(excuse, path="/output/entry.txt"):
    """Write the validated excuse to path, creating parent dirs as needed."""
    import os

    validate_excuse(excuse)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(excuse)
    return path


def main():
    excuse = load_excuse()
    path = write_entry(excuse)
    print("Wrote %d chars to %s" % (len(excuse), path))


if __name__ == "__main__":
    main()

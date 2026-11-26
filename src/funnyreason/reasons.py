import random
from pathlib import Path

REASONS = (
    Path(__file__)
    .with_name("reasons.txt")
    .read_text(encoding="utf-8")
    .splitlines()
)


def random_reason():
    return random.choice(REASONS)

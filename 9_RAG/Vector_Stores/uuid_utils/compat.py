from __future__ import annotations

from datetime import datetime, timezone
import secrets
import uuid


def uuid7() -> uuid.UUID:
    unix_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    unix_ms &= (1 << 48) - 1
    rand_a = secrets.randbits(12)
    rand_b = secrets.randbits(62)

    value = (unix_ms << 80) | (0x7 << 76) | (rand_a << 64) | (0x2 << 62) | rand_b
    return uuid.UUID(int=value)

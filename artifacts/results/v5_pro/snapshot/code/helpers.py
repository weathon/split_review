import re
# ── Leakage detection ────────────────────────────────────────────────
LEAKAGE_WARNING_PATTERNS = [
    r"\bsame paper\b",
    r"\bexact same paper\b",
    r"\bthis exact paper\b",
    r"\bcontains this exact paper\b",
    r"\bthe exact same paper\b",
    r"\bidentical paper\b",
]

def _detect_leakage(text: str) -> list[str]:
    matches = []
    for pattern in LEAKAGE_WARNING_PATTERNS:
        found = re.search(pattern, text, flags=re.IGNORECASE)
        if found:
            matches.append(found.group(0))
    return matches

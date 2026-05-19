patterns = {
    "self_doubt": 0,
    "overthinking": 0,
    "creative_energy": 0,
    "stress": 0
}

def detect_patterns(message: str):
    text = message.lower()

    if "i don't know" in text:
        patterns["self_doubt"] += 1

    if "overwhelmed" in text or "stressed" in text:
        patterns["stress"] += 1

    if "idea" in text or "project" in text:
        patterns["creative_energy"] += 1

    if "why do i" in text:
        patterns["overthinking"] += 1

    return patterns
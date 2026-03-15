import os

SIGNATURE_FILE = "database/signatures.txt"
HASH_FILE = "database/hashes.txt"


def load_signatures():
    if not os.path.exists(SIGNATURE_FILE):
        return []

    with open(SIGNATURE_FILE) as f:
        return [line.strip() for line in f if line.strip()]


def load_hashes():
    if not os.path.exists(HASH_FILE):
        return []

    with open(HASH_FILE) as f:
        return [line.strip() for line in f if line.strip()]

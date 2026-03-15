import os
import hashlib
from quarantine import handle_infected_file


def file_hash(path):
    h = hashlib.sha256()

    try:
        with open(path, "rb") as f:
            while chunk := f.read(4096):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None


def scan_file(file_path, signatures, hashes):
    try:
        with open(file_path, "rb") as f:
            content = f.read().decode(errors="ignore")

            for sig in signatures:
                if sig in content:
                    return True

    except:
        pass

    file_h = file_hash(file_path)

    if file_h and file_h in hashes:
        return True

    return False


def scan_directory(directory, signatures, hashes):
    scanned = 0
    infected = 0

    for root, _, files in os.walk(directory):

        for file in files:

            path = os.path.join(root, file)
            scanned += 1

            if scan_file(path, signatures, hashes):
                infected += 1
                handle_infected_file(path)

    print("\nScan complete")
    print("Files scanned:", scanned)
    print("Threats found:", infected)

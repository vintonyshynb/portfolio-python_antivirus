import os
import shutil

QUARANTINE_DIR = "quarantine"


def quarantine_file(file_path):
    os.makedirs(QUARANTINE_DIR, exist_ok=True)

    name = os.path.basename(file_path)
    new_path = os.path.join(QUARANTINE_DIR, name)

    try:
        shutil.move(file_path, new_path)

        print("File quarantined:", name)

        with open(os.path.join(QUARANTINE_DIR, "log.txt"), "a") as log:
            log.write(f"{name} <- {file_path}\n")

    except Exception as e:
        print("Quarantine failed:", e)


def handle_infected_file(path):
    quarantine_file(path)


def release_files():
    log_path = os.path.join(QUARANTINE_DIR, "log.txt")

    if not os.path.exists(log_path):
        print("No log file")
        return

    with open(log_path) as f:
        lines = f.readlines()

    for line in lines:

        if " <- " not in line:
            continue

        name, original = line.strip().split(" <- ")

        src = os.path.join(QUARANTINE_DIR, name)

        try:
            os.makedirs(os.path.dirname(original), exist_ok=True)
            shutil.move(src, original)

            print("Restored:", name)

        except Exception as e:
            print("Restore failed:", e)

    open(log_path, "w").close()

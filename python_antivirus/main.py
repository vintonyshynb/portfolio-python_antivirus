from scanner import scan_directory
from monitor import real_time_monitor
from quarantine import release_files
from utils import load_signatures, load_hashes
import os


def main():
    print("=== Python Security Scanner ===")
    print("1. Scan folder")
    print("2. Real-time monitor")
    print("3. Restore quarantined files")
    print("4. Exit")

    choice = input("Choose option: ").strip()

    signatures = load_signatures()
    hashes = load_hashes()

    if choice == "1":
        path = input("Enter path to scan: ").strip()

        if os.path.exists(path):
            scan_directory(path, signatures, hashes)
        else:
            print("Invalid path.")

    elif choice == "2":
        path = input("Enter path to monitor: ").strip()

        if os.path.exists(path):
            real_time_monitor(path, signatures, hashes)
        else:
            print("Invalid path.")

    elif choice == "3":
        release_files()

    elif choice == "4":
        print("Goodbye")

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()

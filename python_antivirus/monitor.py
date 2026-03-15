import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from scanner import scan_file
from quarantine import handle_infected_file


class MonitorHandler(FileSystemEventHandler):

    def __init__(self, signatures, hashes):
        self.signatures = signatures
        self.hashes = hashes

    def on_created(self, event):

        if event.is_directory:
            return

        path = event.src_path
        print("New file:", path)

        if scan_file(path, self.signatures, self.hashes):
            handle_infected_file(path)


def real_time_monitor(path, signatures, hashes):
    print("Monitoring:", path)

    handler = MonitorHandler(signatures, hashes)
    observer = Observer()

    observer.schedule(handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()
        print("Monitoring stopped")

    observer.join()

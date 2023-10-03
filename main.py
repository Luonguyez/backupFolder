import shutil
import time
import threading
import datetime

with open('file_paths.txt', 'r') as f:
    backup_pairs = [line.strip().split() for line in f.readlines()]

def backup_pair(source, dest, interval):
    while True:
        try:
            shutil.copytree(source, dest, dirs_exist_ok=True)
            print(f'Backup successful at {datetime.datetime.now()}: {source} -> {dest}')
        except Exception as e:
            print(f'Error occurred during backup: {e}')
        time.sleep(interval)
        print('Backing up ...')

threads = []
for source, dest, interval in backup_pairs:
    t = threading.Thread(target=backup_pair, args=(source, dest, int(interval)))
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()

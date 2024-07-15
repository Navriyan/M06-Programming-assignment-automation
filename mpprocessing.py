import multiprocessing
import time
import random
from datetime import datetime

def worker():
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    print(f"Process {multiprocessing.current_process().name} - Current time: {datetime.now()}")

if __name__ == "__main__":
    processes = []

    # Create three processes
    for i in range(3):
        process = multiprocessing.Process(target=worker, name=f"Process-{i+1}")
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

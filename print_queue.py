import threading

class PrintQueueManager:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.lock = threading.Lock()
        self.time = 0

    def show_status(self):
        with self.lock:
            if self.size == 0:
                print("Queue is empty.")
                return

            print(f"\n[STATUS] Snapshot at Tick {self.time}:")
            index = self.front
            count = 0
            while count < self.size:
                job = self.queue[index]
                print(f"{job['job_id']} - {job['user_id']} - P:{job['priority']} - WT:{job['waiting_time']} - ST:{job['submitted_time']}")
                index = (index + 1) % self.capacity
                count += 1
            print("-" * 30)

    def save_snapshot(self):
        with self.lock:
            with open("queue_snapshot.txt", "w") as f:
                f.write(f"Snapshot at Tick {self.time}:\n")
                index = self.front
                count = 0
                while count < self.size:
                    job = self.queue[index]
                    f.write(f"{job['job_id']} - {job['user_id']} - P:{job['priority']} - WT:{job['waiting_time']} - ST:{job['submitted_time']}\n")
                    index = (index + 1) % self.capacity
                    count += 1
                f.write("-" * 30 + "\n")

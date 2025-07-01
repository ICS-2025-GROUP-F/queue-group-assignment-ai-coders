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
        self.EXPIRY_LIMIT = 15

    def enqueue_job(self, user_id, job_id, priority):
        with self.lock:
            if self.size == self.capacity:
                print("Queue is full. Cannot add new job.")
                return

            job = {
                "user_id": user_id,
                "job_id": job_id,
                "priority": priority,
                "waiting_time": 0,
                "submitted_time": self.time
            }

            self.queue[self.rear] = job
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1

            print(f"[ENQUEUE] Job '{job_id}' from user '{user_id}' added with priority {priority}.")

    def dequeue_job(self):
        with self.lock:
            if self.size == 0:
                print("No jobs in the queue to print.")
                return None

            job = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1

            print(f"[DEQUEUE] Printing job '{job['job_id']}' from user '{job['user_id']}'.")
            return job

    def apply_priority_aging(self):
        with self.lock:
            index = self.front
            count = 0
            while count < self.size:
                job = self.queue[index]
                job['waiting_time'] = self.time - job['submitted_time']
                if job['waiting_time'] >= 5:
                    job['priority'] += 1
                index = (index + 1) % self.capacity
                count += 1

    def remove_expired_jobs(self):
        with self.lock:
            new_queue = [None] * self.capacity
            new_front = 0
            new_rear = 0
            new_size = 0

            index = self.front
            count = 0
            removed = 0

            while count < self.size:
                job = self.queue[index]
                if (self.time - job['submitted_time']) <= self.EXPIRY_LIMIT:
                    new_queue[new_rear] = job
                    new_rear = (new_rear + 1) % self.capacity
                    new_size += 1
                else:
                    removed += 1
                index = (index + 1) % self.capacity
                count += 1

            self.queue = new_queue
            self.front = 0
            self.rear = new_rear
            self.size = new_size

            if removed > 0:
                print(f"[EXPIRY] Removed {removed} expired job(s) at time {self.time}.")

    def handle_simultaneous_submissions(self, jobs):
        threads = []

        def submit_job(job):
            self.enqueue_job(job['user_id'], job['job_id'], job['priority'])

        for job in jobs:
            t = threading.Thread(target=submit_job, args=(job,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def tick(self):
        self.time += 1
        print(f"[TICK] Time advanced to {self.time}")

        self.apply_priority_aging()
        self.remove_expired_jobs()
        self.save_snapshot()
        self.show_status()

    def show_status(self):
        with self.lock:
            if self.size == 0:
                print("Queue is currently empty.")
                return

            print(f"\n[STATUS] Snapshot at Tick {self.time}:")
            index = self.front
            count = 0
            while count < self.size:
                job = self.queue[index]
                print(f"User: {job['user_id']} | Job: {job['job_id']} | Priority: {job['priority']} | Waiting Time: {job['waiting_time']} | Submitted: {job['submitted_time']}")
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


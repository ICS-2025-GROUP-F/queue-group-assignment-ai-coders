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

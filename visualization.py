def save_snapshot(self):
        with open("queue_snapshot.txt","w")as f:
            f.write(f"Snapshot at Tick{self.time}:\n")
            for job in self.queue:
                f.write(f"{job['job_id']} - {job['user_id']} - P:{job['priority']} - WT:{job['waiting_time']}\n")
            f.write("-" * 30 + "\n")

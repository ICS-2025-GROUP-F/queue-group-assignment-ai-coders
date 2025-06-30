def tick(self):
    self.global_time += 1
    print(f"[TICK] Time advanced to {self.global_time}")

    for job in self.queue:
        job['waiting_time'] = self.global_time - job['submitted_time']

    self.apply_priority_aging()
    self.remove_expired_jobs()

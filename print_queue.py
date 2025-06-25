class PrintQueueManager:
   def __init__(self):
       self.queue = []
       self.time = 0
       self.EXPIRY_LIMIT = 15
   def remove_expired_jobs(self):
       before = len(self.queue)
       self.queue = [job for job in self.queue if (self.time - job["submitted_time"]) <= self.EXPIRY_LIMIT]
       after = len(self.queue)
       removed = before - after
       if removed > 0:
           print(f"[INFO] Removed {removed} expired job(s) at time {self.time}")
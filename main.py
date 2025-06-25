from print_queue import PrintQueueManager
manager = PrintQueueManager()
manager.time = 20
manager.queue = [
   {"user_id": "A", "job_id": 1, "priority": 2, "waiting_time": 15, "submitted_time": 2},
   {"user_id": "B", "job_id": 2, "priority": 1, "waiting_time": 8, "submitted_time": 12},
   {"user_id": "C", "job_id": 3, "priority": 3, "waiting_time": 2, "submitted_time": 18},
]
print("Before removal:")
for job in manager.queue:
   print(job)
manager.remove_expired_jobs()
print("\nAfter removal:")
for job in manager.queue:
   print(job)
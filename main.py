from print_queue import PrintQueueManager

if __name__ == "__main__":
    pq = PrintQueueManager(capacity=5)

    pq.enqueue_job("alice", "jobA", 1)
    pq.enqueue_job("bob", "jobB", 2)
    pq.enqueue_job("carol", "jobC", 1)

    pq.tick()  # time advances, aging, expiry, snapshot, status
    pq.dequeue_job()
    pq.show_status()

    jobs = [
        {"user_id": "dave", "job_id": "jobD", "priority": 1},
        {"user_id": "eve", "job_id": "jobE", "priority": 2},
    ]
    pq.handle_simultaneous_submissions(jobs)
    pq.tick()

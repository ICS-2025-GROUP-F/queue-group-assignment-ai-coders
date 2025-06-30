class PrintQueueManager:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue_job(self, user_id, job_id, priority):
        if self.size == self.capacity:
            print("Queue is full. Cannot add new job.")
            return

        job = {
            "user_id": user_id,
            "job_id": job_id,
            "priority": priority,
            "waiting_time": 0
        }

        self.queue[self.rear] = job
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

        print(f"Job '{job_id}' from user '{user_id}' added with priority {priority}.")

    def print_job(self):
        if self.size == 0:
            print("No jobs in the queue to print.")
            return

        job = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        print(f"Printing job '{job['job_id']}' from user '{job['user_id']}'.")

    def show_status(self):
        if self.size == 0:
            print("Queue is currently empty.")
            return

        print("\nQueue Status:")
        index = self.front
        count = 0
        while count < self.size:
            job = self.queue[index]
            print(f"User: {job['user_id']} | Job: {job['job_id']} | Priority: {job['priority']} | Waiting Time: {job['waiting_time']}s")
            index = (index + 1) % self.capacity
            count += 1
        print()

if __name__ == "__main__":
    pq = PrintQueueManager(capacity=5)

    pq.enqueue_job("alice", "jobA", 3)
    pq.enqueue_job("bob", "jobB", 2)
    pq.enqueue_job("carol", "jobC", 1)

    pq.show_status()

    pq.print_job()

    pq.show_status()

    pq.enqueue_job("dave", "jobD", 5)
    pq.enqueue_job("eve", "jobE", 4)
    pq.enqueue_job("frank", "jobF", 2)

    pq.show_status()

class PrintQueueManager:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.aging_interval = 5  # Aging interval in seconds

    def enqueue_job(self, user_id, job_id, priority):
        if self.size == self.capacity:
            print("⚠️ Queue is full. Cannot add new job.")
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

        print(f"✅ Job '{job_id}' from user '{user_id}' added with priority {priority}.")
        
        # Reorder queue based on priority after adding new job
        self.reorder_queue_by_priority()

    def print_job(self):
        if self.size == 0:
            print("🛑 No jobs in the queue to print.")
            return

        job = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        print(f"🖨️ Printing job '{job['job_id']}' from user '{job['user_id']}'.")

    def show_status(self):
        if self.size == 0:
            print("📭 Queue is currently empty.")
            return

        print("\n📋 Queue Status:")
        index = self.front
        count = 0
        while count < self.size:
            job = self.queue[index]
            print(f"🔸 User: {job['user_id']} | Job: {job['job_id']} | Priority: {job['priority']} | Waiting Time: {job['waiting_time']}s")
            index = (index + 1) % self.capacity
            count += 1
        print()
        
    def apply_priority_aging(self):
        """
        Increment job priority after a configurable aging interval.
        Higher priority number means higher priority.
        """
        if self.size == 0:
            return
            
        index = self.front
        count = 0
        while count < self.size:
            job = self.queue[index]
            # Apply aging - if waiting time is a multiple of aging interval, increase priority
            if job['waiting_time'] > 0 and job['waiting_time'] % self.aging_interval == 0:
                job['priority'] += 1
                print(f"⏫ Job '{job['job_id']}' priority increased to {job['priority']} due to aging.")
            
            index = (index + 1) % self.capacity
            count += 1
            
        # Reorder queue after applying aging
        self.reorder_queue_by_priority()
    
    def reorder_queue_by_priority(self):
        """
        Reorder the queue based on job priorities.
        Higher priority jobs move to the front.
        If priorities are equal, jobs with longer waiting time go first.
        """
        if self.size <= 1:
            return
            
        # Extract all jobs from the queue
        jobs = []
        index = self.front
        count = 0
        while count < self.size:
            jobs.append(self.queue[index])
            self.queue[index] = None
            index = (index + 1) % self.capacity
            count += 1
        
        # Sort jobs by priority (higher number = higher priority)
        # If priorities are equal, sort by waiting time (higher waiting time first)
        jobs.sort(key=lambda x: (-x['priority'], -x['waiting_time']))
        
        # Reset queue pointers
        self.front = 0
        self.rear = 0
        self.size = 0
        
        # Re-insert jobs in priority order
        for job in jobs:
            self.queue[self.rear] = job
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1
    
    def tick(self):
        """
        Simulate time passing by one second.
        Update waiting times for all jobs and apply aging.
        """
        if self.size == 0:
            print("⏱️ Tick: Queue is empty.")
            return
            
        print("⏱️ Tick: Updating waiting times...")
        
        # Update waiting time for all jobs
        index = self.front
        count = 0
        while count < self.size:
            job = self.queue[index]
            job['waiting_time'] += 1
            index = (index + 1) % self.capacity
            count += 1
        
        # Apply priority aging
        self.apply_priority_aging()

if __name__ == "__main__":
    pq = PrintQueueManager(capacity=5)

    pq.enqueue_job("alice", "jobA", 3)
    pq.enqueue_job("bob", "jobB", 2)
    pq.enqueue_job("carol", "jobC", 1)

    pq.show_status()

    # Simulate time passing
    for _ in range(6):
        pq.tick()
    
    pq.show_status()

    pq.print_job()

    pq.show_status()

    pq.enqueue_job("dave", "jobD", 5)
    pq.enqueue_job("eve", "jobE", 4)
    pq.enqueue_job("frank", "jobF", 2)

    pq.show_status()

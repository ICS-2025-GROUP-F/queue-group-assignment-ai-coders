# QUEUE-GROUP-ASSIGNMENT Submission

## Group Name: AI-CODERS

## Group Members and Contributions

### Member 2: Student Number 184587
- **Module**: Priority & Aging System
- **Contribution**: Implemented the priority-based ordering of jobs, priority aging system that increments job priority after a configurable aging interval, and tie-breaking by waiting time.
- **Functions implemented**:
  - `apply_priority_aging()`: Increments job priority after a configurable aging interval
  - `reorder_queue_by_priority()`: Reorders the queue based on job priorities and waiting times
  - Enhanced `tick()`: Updates waiting times and applies aging logic

## Instructions on How to Run the Code

1. Ensure you have Python 3.6 or higher installed.
2. Clone the repository to your local machine.
3. Navigate to the repository directory.
4. Run the main program:
   ```
   python code.py
   ```

## Features Implemented

### Priority & Aging System
- Jobs are ordered by priority (higher number = higher priority)
- Priority aging is applied at configurable intervals (default: every 5 seconds)
- When jobs have the same priority, the one with longer waiting time is prioritized
- The queue is automatically reordered whenever priorities change

## Sample Output

The program will show:
- Jobs being added to the queue with their initial priorities
- Time passing (ticks) and waiting times increasing
- Priority aging being applied when waiting time reaches multiples of the aging interval
- Queue status showing the current order of jobs based on priority and waiting time 
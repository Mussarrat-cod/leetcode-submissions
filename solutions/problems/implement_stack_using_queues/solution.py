from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Step 1: push to q2
        self.q2.append(x)

        # Step 2: move all from q1 → q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Step 3: swap
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0
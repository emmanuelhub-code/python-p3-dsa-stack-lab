class Stack:
    def __init__(self, items=None, limit=None):
        """Initialize stack with optional list of items and optional limit."""
        self.items = items[:] if items else []
        self.limit = limit

    def push(self, value):
        """Push a value onto the stack if there is room. Raise OverflowError if full."""
        if self.limit is not None and len(self.items) >= self.limit:
            raise OverflowError("Stack is full")
        self.items.append(value)
        return self

    def pop(self):
        """Pop the top value off the stack. Return None if empty."""
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top value without removing it. Return None if empty."""
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def isEmpty(self):
        """Return True if the stack is empty."""
        return len(self.items) == 0

    def full(self):
        """Return True if the stack is full (limit reached)."""
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, value):
        """
        Return the distance from the top of the stack to the value.
        Top of the stack is distance 0. Return -1 if not found.
        """
        for i in range(len(self.items)-1, -1, -1):
            if self.items[i] == value:
                return len(self.items) - 1 - i
        return -1

    def __str__(self):
        """Return a string representation of the stack."""
        return f"Stack: {self.items}"

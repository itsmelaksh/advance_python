class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # O(1)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # O(1)
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from empty stack")

    # Insert methods
    def insert_at_begin(self, item):
        self.data.insert(0, item)  # O(n)

    def insert_at_end(self, item):
        self.data.append(item)  # O(1)

    def insert_at(self, index, item):
        if 0 <= index <= len(self.data):
            self.data.insert(index, item)  # O(n)
        else:
            raise IndexError("Invalid index")

    # Delete methods
    def delete_at_begin(self):
        if not self.is_empty():
            return self.data.pop(0)  # O(n)
        raise IndexError("Delete from empty list")

    def delete_at_end(self):
        if not self.is_empty():
            return self.data.pop()  # O(1)
        raise IndexError("Delete from empty list")

    def delete_at(self, index):
        if not self.is_empty() and 0 <= index < len(self.data):
            return self.data.pop(index)  # O(n)
        raise IndexError("Invalid index or empty list")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # 30
print(s.peek())  # 20
print(s.size())  # 2

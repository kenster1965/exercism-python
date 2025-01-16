"""Circular Buffer"""

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
    message: explanation of the error.
    """
    def __init__(self, message="Circular buffer is full"):
        """
        BufferFullException
        :param message: str: Explanation of the error.
        """
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
    message: explanation of the error.
    """
    def __init__(self, message="Circular buffer is empty"):
        """
        BufferEmptyException
        :param message: str: Explanation of the error.
        """
        super().__init__(message)


class CircularBuffer:
    """Circular Buffer"""
    def __init__(self, capacity):
        """
        CircularBuffer
        :param capacity: int: The maximum number of items that can be stored in the buffer.
        """
        self.capacity = capacity
        self.buffer = [None] * capacity  # Fixed-size buffer
        self.start = 0  # Points to the oldest item
        self.size = 0   # Tracks the number of items in the buffer

    def read(self):
        """
        Read the oldest item in the buffer.
        :return: The oldest item in the buffer.
        :raises BufferEmptyException: If the buffer is empty.
        """
        if self.size == 0:
            raise BufferEmptyException()
        data = self.buffer[self.start]
        self.buffer[self.start] = None  # Clear the slot
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return data

    def write(self, data):
        """
        Write a new item to the buffer.
        :param data: The item to be written.
        :raises BufferFullException: If the buffer is full.
        """
        if self.size == self.capacity:
            raise BufferFullException()
        end = (self.start + self.size) % self.capacity
        self.buffer[end] = data
        self.size += 1

    def overwrite(self, data):
        """
        Write a new item to the buffer.
        If the buffer is full, overwrite the oldest item.
        :param data: The item to be written.
        """
        if self.size == self.capacity:
            self.buffer[self.start] = data
            self.start = (self.start + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        """
        Clear the buffer.
        """
        self.buffer = [None] * self.capacity
        self.start = 0
        self.size = 0

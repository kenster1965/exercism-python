import io
import socket
import errno
import os
class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):
        # Support context management
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Delegate __exit__ to the wrapped object
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        # Return self for iteration
        return self

    def __next__(self):
        # Read the next line using readline
        line = self.readline()
        if line == b"":  # End of file
            raise StopIteration
        self._read_bytes += len(line)
        self._read_ops += 1
        return line

    def read(self, size=-1):
        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        return data

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        written = super().write(b)
        self._write_bytes += written
        self._write_ops += 1
        return written

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops

class MeteredSocket:
    def __init__(self, socket):
        self._socket = socket
        self._closed = False
        self._recv_ops = 0
        self._recv_bytes = 0
        self._send_ops = 0
        self._send_bytes = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._closed = True
        # Call the wrapped socket's __exit__ method
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    @property
    def recv_ops(self):
        return self._recv_ops

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def send_ops(self):
        return self._send_ops

    @property
    def send_bytes(self):
        return self._send_bytes

    def recv(self, bufsize, flags=0):
        if self._closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        if not isinstance(flags, int):
            raise TypeError("integer is required")
        data = self._socket.recv(bufsize, flags)
        self._recv_ops += 1
        self._recv_bytes += len(data)
        return data

    def send(self, data, flags=0):
        if self._closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        if not isinstance(flags, int):
            raise TypeError("integer is required")
        sent_len = self._socket.send(data, flags)
        self._send_ops += 1
        self._send_bytes += sent_len
        return sent_len

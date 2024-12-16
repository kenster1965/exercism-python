"""This module provides classes for metering I/O operations on files and sockets."""
import io
import errno
import os

class MeteredFile(io.BufferedRandom):
    """With subclassing."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):
        """Return self to allow usage like `with MeteredFile(...) as f:`."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Return the result of the superclass's __exit__ method."""
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        """Return self to allow usage like `for line in f:`."""
        return self

    def __next__(self):
        """Return the next line from the file."""
        data = super().readline()
        self._read_bytes += len(data)
        self._read_ops += 1
        if data:
            return data
        else:
            raise StopIteration

    def read(self, size=-1):
        """Read up to size bytes from the file."""
        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        return data

    @property
    def read_bytes(self):
        """Return the number of bytes read from the file."""
        return self._read_bytes

    @property
    def read_ops(self):
        """Return the reading of the file."""
        return self._read_ops

    def write(self, b):
        """Write the given bytes to the file."""
        write_len = super().write(b)
        self._write_bytes += write_len
        self._write_ops += 1
        return write_len

    @property
    def write_bytes(self):
        """Return the number of bytes written to the file."""
        return self._write_bytes

    @property
    def write_ops(self):
        """Return the number of write operations."""
        return self._write_ops

class MeteredSocket:
    """MeteredSocket` class."""
    def __init__(self, socket):
        """Initialize the MeteredSocket object."""
        self._socket = socket
        self._closed = False
        self._recv_ops = 0
        self._recv_bytes = 0
        self._send_ops = 0
        self._send_bytes = 0

    def __enter__(self):
        """Return self to allow usage like `with MeteredSocket(...) as s:`."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Return the result of the wrapped socket's __exit__ method."""
        self._closed = True
        # Call the wrapped socket's __exit__ method
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    @property
    def recv_ops(self):
        """Return the number of receive operations."""
        return self._recv_ops

    @property
    def recv_bytes(self):
        """Return the number of bytes received."""
        return self._recv_bytes

    @property
    def send_ops(self):
        """Return the number of send operations."""
        return self._send_ops

    @property
    def send_bytes(self):
        """Return the number of bytes sent."""
        return self._send_bytes

    def recv(self, bufsize, flags=0):
        """Receive data from the socket."""
        if self._closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        if not isinstance(flags, int):
            raise TypeError("integer is required")
        data = self._socket.recv(bufsize, flags)
        self._recv_ops += 1
        self._recv_bytes += len(data)
        return data

    def send(self, data, flags=0):
        """Send data to the socket."""
        if self._closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        if not isinstance(flags, int):
            raise TypeError("integer is required")
        sent_len = self._socket.send(data, flags)
        self._send_ops += 1
        self._send_bytes += sent_len
        return sent_len

import io
import socket
import errno
import os

class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def read(self, size=-1):
        pass

    @property
    def read_bytes(self):
        pass

    @property
    def read_ops(self):
        pass

    def write(self, b):
        pass

    @property
    def write_bytes(self):
        pass

    @property
    def write_ops(self):
        pass


class MeteredSocket:
    def __init__(self, socket):
        self._socket = socket
        self._closed = False
        self.recv_ops = 0
        self.recv_bytes = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._closed = True
        # Call the wrapped socket's __exit__ method
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize):
        if self._closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        data = self._socket.recv(bufsize)
        self.recv_ops += 1
        self.recv_bytes += len(data)
        return data

    def send(self, data):
        if self._closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        return self._socket.send(data)

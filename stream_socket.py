# stream_socket.py
# simple socket client test
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("httpbin.org",8000))

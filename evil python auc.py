import socket
import threading

s = socket.create_connection(("ip", port))

threading.Thread(target=lambda: print(s.recv(4096).decode()), daemon=True).start()

while True:
    s.sendall((input() + "\n").encode())

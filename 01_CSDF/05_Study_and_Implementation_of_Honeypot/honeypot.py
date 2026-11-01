# CSDF-5: Honeypot
# Program (honeypot.py): low-interaction honeypot
import socket
import threading
import time
import datetime
import sys

PORTS = {
    2121: b"220 FTP Server ready\r\n",
    2323: b"Login: ",
    8081: b"HTTP/1.1 200 OK\r\nServer: Apache/2.2\r\n\r\n"
}
LOG = "honeypot.log"

def log(msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    print(line)
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

def handle(conn, addr, port):
    log(f"[CONNECT] {addr[0]}:{addr[1]} -> port {port}")
    try:
        conn.sendall(PORTS[port])
        conn.settimeout(2)
        data = conn.recv(1024)
        if data:
            log(f"[DATA]    {addr[0]} sent {data.strip()!r}")
    except socket.timeout:
        pass
    except Exception:
        pass
    finally:
        conn.close()
        log(f"[CLOSED]  {addr[0]}:{addr[1]}")

def listen(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", port))
    s.listen(5)
    while True:
        c, a = s.accept()
        threading.Thread(target=handle, args=(c, a, port), daemon=True).start()

def simulate_traffic():
    """Simulates 4 test connections to demonstrate low-interaction honeypot."""
    time.sleep(0.5)
    tests = [
        (2121, b"USER admin\r\n"),
        (2323, b"root\r\n"),
        (8081, b"GET /admin HTTP/1.1\r\n\r\n"),
        (2121, b"USER test\r\n"),
    ]
    for port, payload in tests:
        try:
            sock = socket.socket()
            sock.connect(("127.0.0.1", port))
            sock.recv(1024)  # Receive banner from honeypot
            sock.sendall(payload)
            time.sleep(0.3)
            sock.close()
        except Exception:
            pass

if __name__ == "__main__":
    for p in PORTS:
        threading.Thread(target=listen, args=(p,), daemon=True).start()
    log(f"Honeypot listening on ports {list(PORTS)}")

    # Automatically simulate 4 test connections unless disabled
    if "--no-simulate" not in sys.argv:
        threading.Thread(target=simulate_traffic, daemon=True).start()

    # Sleep duration: default 3 seconds for demonstration, or custom seconds from CLI argument
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    duration = float(args[0]) if args else 3.0
    time.sleep(duration)

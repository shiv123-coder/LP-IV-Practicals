"""
CSDF Practical No. 4: Log Capturing and Event Correlation
Program: log_correlate.py (from CSDF4.pdf)
"""

import os
from collections import defaultdict, Counter
from datetime import datetime

log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "access.log") if "__file__" in globals() else "access.log"

users, sites = defaultdict(lambda: [0, 0, 0]), Counter()   # per user: [requests, bytes, hits]
denied, auth_fail, downloads = defaultdict(Counter), Counter(), []

for line in open(log_path, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    ts, el, ip, code, size, method, url, user, hier, mime = line.split()
    status, size = code.split("/")[1], int(size)
    host = url.split("/")[2]
    u = users[ip]; u[0] += 1; u[1] += size
    if "HIT" in code: u[2] += 1
    sites[host] += 1
    if "DENIED" in code:  denied[ip][host] += 1
    if status == "407":   auth_fail[ip] += 1
    if size > 100000:     downloads.append((datetime.fromtimestamp(float(ts)).strftime("%d/%m/%Y %H:%M:%S"), ip, url, size))

print("=== SUMMARY PER CLIENT ===")
print(f"{'IP':15} {'REQ':>4} {'BYTES':>8} {'CACHE-HIT%':>10}")
for ip, (r, b, h) in sorted(users.items(), key=lambda x: -x[1][1]):
    print(f"{ip:15} {r:4d} {b:8d} {100*h/r:9.0f}%")

print("\n=== TOP SITES ===")
for s, c in sites.most_common(3):
    print(f"{s:25} {c} requests")

print("\n=== DOWNLOADS (> 100 KB) ===")
for d in downloads:
    print(*d)

print("\n=== EVENT CORRELATION ALERTS ===")
for ip, c in denied.items():
    for s, n in c.items():
        if n >= 3:
            print(f"[ALERT] {ip} repeatedly denied for {s} ({n} times in 2 s) -> possible policy violation")

for ip, n in auth_fail.items():
    if n >= 3:
        print(f"[ALERT] {ip} had {n} authentication failures (HTTP 407) -> possible brute force / bad credentials")

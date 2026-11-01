import os
import re
import sys

print("===== EMAIL HEADER ANALYZER =====")
print("Paste the raw email header.")
print("Type END on a new line when finished (or press Enter twice to use sample_header.txt):\n")

lines = []

while True:
    try:
        line = input()
    except EOFError:
        break
    if line.strip() == "END":
        break
    if not lines and line.strip() == "":
        break
    lines.append(line)

# Fallback to sample_header.txt if empty input is submitted
sample_path = os.path.join(os.path.dirname(__file__), "sample_header.txt") if "__file__" in globals() else "sample_header.txt"
if not any(l.strip() for l in lines) and os.path.exists(sample_path):
    print("[INFO] No header pasted; automatically analyzing 'sample_header.txt'...")
    with open(sample_path, "r", encoding="utf-8") as f:
        header = f.read()
else:
    header = "\n".join(lines)

# Extract important email fields
fields = [
    "From",
    "To",
    "Subject",
    "Date",
    "Message-ID",
    "Reply-To",
    "Return-Path"
]

print("\n===== HEADER ANALYSIS =====")

for field in fields:
    match = re.search(
        r"(?im)^" + re.escape(field) + r":\s*(.*(?:\n[ \t]+.*)*)",
        header
    )

    if match:
        print(field + ":", " ".join(match.group(1).split()))

# Extract IP addresses
ips = re.findall(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    header
)

print("\n===== IP ADDRESSES =====")
if ips:
    for ip in dict.fromkeys(ips):
        print(ip)
else:
    print("No IPv4 addresses found.")

# Show email authentication results
print("\n===== AUTHENTICATION =====")

for check in ["SPF", "DKIM", "DMARC"]:
    results = re.findall(
        r"\b" + check.lower() + r"\s*=\s*(pass|fail|softfail|neutral|none|temperror|permerror)",
        header,
        re.IGNORECASE
    )

    if results:
        print(check + ":", ", ".join(
            result.upper() for result in results
        ))
    else:
        print(check + ": Not found in header")

# Show Received fields (email delivery path)
print("\n===== EMAIL DELIVERY PATH =====")

received = re.findall(
    r"(?im)^Received:\s*(.*(?:\n[ \t]+.*)*)",
    header
)

if received:
    for i, item in enumerate(received, 1):
        print(str(i) + ".", " ".join(item.split()))
else:
    print("No Received fields found.")

print("\n===== ANALYSIS COMPLETED =====")
print("Note: Results are extracted from the supplied header.")
print("This program does not prove that an email is safe.")

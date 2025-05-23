#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Total file size
- Count of status codes
"""

import sys
import re
import signal

status_codes = {
    "200": 0, "301": 0, "400": 0,
    "401": 0, "403": 0, "404": 0,
    "405": 0, "500": 0
}
total_size = 0
line_count = 0

def print_stats():
    """Prints the metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) >= 7:

            status_code = parts[-2]
            file_size = parts[-1]
            if status_code in status_codes:
                try:
                    status_codes[status_code] += 1
                except Exception:
                    pass
            try:
                total_size += int(file_size)
            except Exception:
                pass
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
else:
    print_stats()
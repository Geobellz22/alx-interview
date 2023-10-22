#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys
import signal

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
line_count = 0


def print_statistics(signal, frame):
    global line_count
    global total_size
    global status_codes

    print("File size: {0}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{0}: {1}".format(code, status_codes[code]))
    line_count = 0
    status_codes = dict.fromkeys(status_codes, 0)
    total_size = 0


signal.signal(signal.SIGINT, print_statistics)

for line in sys.stdin:
    parts = line.split(' ')
    if len(parts) >= 7:
        status_code = parts[-2]
        size = parts[-1]
        if status_code in status_codes:
            status_codes[status_code] += 1
        if size.isdigit():
            total_size += int(size)
        line_count += 1
    if line_count >= 10:
        print_statistics(None, None)

print_statistics(None, None)

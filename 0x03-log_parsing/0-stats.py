#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
counter = 0
total_size = 0

try:
    for line in sys.stdin:
        line_items = line.split(" ")
        if len(line_items) > 4:
            status_code = line_items[-2]
            file_size = line_items[-1]
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += int(file_size)
            counter += 1

        if counter == 10:
            counter = 0
            print(f"File size: {total_size}")
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print(f"{key}: {value}")

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print(f"{key}: {value}")


finally:
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print(f"{key}: {value}")

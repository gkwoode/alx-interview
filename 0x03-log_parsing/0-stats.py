#!/usr/bin/python3
""" Write a script that reads stdin line by line and computes metrics: """

import signal
import sys

def print_statistics(status_counts, total_size):
    print("Total file size: File size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        date = parts[3][1:] + " " + parts[4][:-1]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, date, status_code, file_size
    except (IndexError, ValueError):
        return None

def main():
    status_counts = {}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            data = parse_line(line)
            if data is not None:
                _, _, status_code, file_size = data
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(status_counts, total_size)
    except KeyboardInterrupt:
        print_statistics(status_counts, total_size)
        sys.exit(0)

if __name__ == "__main__":
    main()

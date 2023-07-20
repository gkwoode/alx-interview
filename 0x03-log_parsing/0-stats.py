#!/usr/bin/python3
""" Write a script that reads stdin line by line and computes metrics: """

import sys

def print_statistics(total_size, status_codes):
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        date = parts[1] + " " + parts[2]
        status_code = int(parts[-3])
        file_size = int(parts[-2])
        return ip_address, date, status_code, file_size
    except (ValueError, IndexError):
        return None

def main():
    total_size = 0
    status_codes = {}

    try:
        for line_count, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            parsed_data = parse_line(line)
            if not parsed_data:
                continue

            _, _, status_code, file_size = parsed_data

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print("\nInterrupted by user. Printing current statistics:")
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()

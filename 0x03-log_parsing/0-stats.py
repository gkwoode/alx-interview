#!/usr/bin/python3
"""Log Parsing"""

import sys


def print_statistics(total_size, status_counts):
    """Print statistics"""

    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def process_log_line(line, total_size, status_counts):
    """Process  log line"""

    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[8]
        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                total_size += int(parts[9])
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1
    return total_size, status_counts


def main():
    """Main function"""

    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            total_size, status_counts = process_log_line(
                    line, total_size, status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (CTRL + C)
        print_statistics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()

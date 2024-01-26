#!/usr/bin/python3

"""cript that reads stdin and computes metrics"""
import sys
import signal


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                      404: 0, 405: 0, 500: 0}
line_count = 0


def print_metrics():
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")


def handle_interrupt(signal, frame):
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        # Parse the input line
        parts = line.split()
        if len(parts) == 7:
            ip, _, _, date, _, request, status_code, file_size = parts
            if request == '"GET' and file_size.isdigit():
                total_file_size += int(file_size)
                status_code = int(status_code)
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                line_count += 1

                # Print metrics every 10 lines
                if line_count % 10 == 0:
                    print_metrics()
        else:
            # Skip lines with incorrect format
            continue

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_metrics()
    sys.exit(0)

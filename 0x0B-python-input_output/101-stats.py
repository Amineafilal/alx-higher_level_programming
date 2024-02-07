#!/usr/bin/python3
""" This module hat reads stdin line by line and computes metrics """
import sys

def print_metrics(total_size, status_counts):
    """Prints the computed metrics."""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        print("{}: {}".format(status_code, status_counts[status_code]))

def parse_line(line):
    """Parses a line according to the input format."""
    parts = line.strip().split()
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            status_code, file_size = parse_line(line)
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        raise

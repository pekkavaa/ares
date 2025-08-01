#!/usr/bin/env python3
import sys
import os
from statistics import mean, median

def compute_file_stats(directory):
    sizes = []
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                sizes.append(os.path.getsize(filepath))
            except OSError:
                continue
    if not sizes:
        return None
    return {
        'min': min(sizes),
        'max': max(sizes),
        'mean': mean(sizes),
        'median': median(sizes)
    }

stats = compute_file_stats(sys.argv[1])
print(stats)

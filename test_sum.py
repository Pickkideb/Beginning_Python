#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

max_val = max(arr)
min_val = min(arr)

if int(max_val) == int(min_val):
    total_max = sum(arr)
    total_min = sum(arr)
else:
    total_max = int(0)
    total_min = int(0)
    i = int(0)
    j = int(0)

    length = int(len(arr))

    for i in range(length):
        total_max += (int(arr[i]) if int(arr[i]) != int(min_val) else 0)

    for j in range(length):
        total_min += (int(arr[j]) if int(arr[j]) != int(max_val) else 0)

print(total_min, total_max)

print("sample_check")

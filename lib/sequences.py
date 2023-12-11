#!/usr/bin/env python3

def print_fibonacci(length):
    out = []
    i = 1
    if length > 0:
        out = [0]
    while len(out) < length:
        out.append(i)
        if len(out) > 1 :
            i = out[-1] + out[-2]
    print(out)

print_fibonacci(10)
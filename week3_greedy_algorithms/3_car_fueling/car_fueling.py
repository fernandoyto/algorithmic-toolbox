# python3
import sys


def compute_min_refills(distance, tank, stops):
    print(distance)
    print(tank)
    print(stops)
    return -1

if __name__ == '__main__':
    d, m, _, stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

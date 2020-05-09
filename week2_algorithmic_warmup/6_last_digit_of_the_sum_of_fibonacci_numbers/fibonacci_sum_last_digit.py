# Uses python3
import sys

def fibonacci_sum_naive(n):
    remainder = n % 60
    return (calc_fib(remainder + 2) - 1) % 10

def calc_fib(n):
    if n <= 1:
        return n

    arr = [0, 1]
    while len(arr) <= n:
        arr.append(arr[-1] + arr[-2])

    return arr[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))

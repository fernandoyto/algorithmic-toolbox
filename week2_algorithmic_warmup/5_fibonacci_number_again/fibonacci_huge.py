# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    arr = [0, 1]
    pisano_period = 0
    while True:
        arr.append((arr[-1] + arr[-2]) % m)
        if arr[-2:] == [0,1]:
            pisano_period = len(arr) - 2
            break

    return calc_fib(n % pisano_period) % m

def calc_fib(n):
    if n <= 1:
        return n

    arr = [0, 1]
    while len(arr) <= n:
        arr.append(arr[-1] + arr[-2])

    return arr[-1]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    arr = [0, 1]
    while len(arr) <= n:
        arr.append(arr[-1] + arr[-2])

    return arr[-1]

n = int(input())
print(calc_fib(n))

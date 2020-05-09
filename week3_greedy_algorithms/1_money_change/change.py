# Uses python3
import sys

def get_change(m):
    coins = 0
    while m > 0:
        if m >= 10:
            coins += 1
            m -= 10
            continue
        if m >= 5:
            coins += 1
            m -= 5
            continue
        coins += 1
        m -= 1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

# Uses python3
import sys

def gcd(a, b):
    current_gcd = min(a, b)
    remainder = max(a, b) % current_gcd
    while remainder != 0:
        return gcd(current_gcd, remainder)
            
    return current_gcd


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))

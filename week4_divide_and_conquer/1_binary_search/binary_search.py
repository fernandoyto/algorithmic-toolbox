# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    
    while left < right:
        mid = int((right + left) / 2)
        
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), sep=' ')

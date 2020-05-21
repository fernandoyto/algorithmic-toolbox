# Uses python3
import sys

def merge(a, b, left, mid, right):
    number_of_inversions = 0

    i, j, k = left, mid, left

    while i <= mid - 1 and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            number_of_inversions += mid - i

        k += 1

    while i <= mid - 1:
        b[k] = a[i]
        i += 1
        k += 1
    
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        a[i] = b[i]

    return number_of_inversions

def merge_sort(a, b, left, right):
    number_of_inversions = 0
    if right > left:
        mid = (left + right) // 2
        number_of_inversions += merge_sort(a, b, left, mid)
        number_of_inversions += merge_sort(a, b, mid + 1, right)
        number_of_inversions += merge(a, b, left, mid + 1, right)

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(merge_sort(a, b, 0, len(a) - 1))

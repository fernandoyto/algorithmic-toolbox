# Uses python3
import sys

def get_majority_element(a):
    min_count = int(len(a) / 2)
    dict = {}

    for el in a:
        if el in dict:
            dict[el] += 1
        else:
            dict[el] = 1
    # print(min_count)
    # print(dict)
    for key in dict.keys():
        # print(key)
        # print(dict[key])
        if dict[key] > min_count:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a))

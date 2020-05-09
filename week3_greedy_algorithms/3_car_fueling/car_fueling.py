# python3
import sys


def compute_min_refills(distance, tank, stops):
    if distance <= tank:
        return 0

    stops.insert(0, 0)
    stops.append(distance)
    refills = 0

    current_index = 0
    next_index = 1
    while stops[current_index] < distance:

        if stops[next_index] == distance and distance - stops[current_index] <= tank:
            return refills

        if stops[next_index + 1] - stops[current_index] > tank:
            current_index = next_index
            next_index += 1
            refills += 1
        else:
            next_index += 1
            continue

        if stops[next_index] - stops[current_index] > tank:
            return -1

    return refills


if __name__ == '__main__':
    input_list = sys.stdin.read().split()
    d = int(input_list[0])
    m = int(input_list[1])
    stops = [int(x) for x in input_list[3:]]
    print(compute_min_refills(d, m, stops))
